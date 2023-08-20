from .view import View
from .model import Model


class Controller:

    model: Model
    view: View

    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.__init_actions()
        self.__connect_button_actions()
        self.view.show()

    def __init_actions(self):
        self.action_read_clinical_data_table = ActionReadClinicalDataTable(self)
        self.action_import_sequencing_table = ActionImportSequencingTable(self)
        self.action_save_clinical_data_table = ActionSaveClinicalDataTable(self)
        self.action_sort_ascending = ActionSortAscending(self)
        self.action_sort_descending = ActionSortDescending(self)
        self.action_delete_selected_rows = ActionDeleteSelectedRows(self)
        self.action_reset_table = ActionResetTable(self)
        self.action_add_new_sample = ActionAddNewSample(self)
        self.action_edit_sample = ActionEditSample(self)
        self.action_export_cbioportal_study = ActionExportCbioportalStudy(self)

    def __connect_button_actions(self):
        for name in self.view.BUTTON_NAME_TO_LABEL.keys():
            button = getattr(self.view, f'button_{name}')
            method = getattr(self, f'action_{name}', None)
            if method is not None:
                button.clicked.connect(method)
            else:
                print(f'WARNING: method "action_{name}" does not exist in the Controller')


class Action:

    model: Model
    view: View

    def __init__(self, controller: Controller):
        self.model = controller.model
        self.view = controller.view


class ActionReadClinicalDataTable(Action):

    def __call__(self):
        file = self.view.file_dialog_open_table()
        if file == '':
            return

        success, msg = self.model.read_clinical_data_table(file=file)
        if not success:
            self.view.message_box_error(msg=msg)

        self.view.refresh_table()


class ActionImportSequencingTable(Action):

    def __call__(self):
        file = self.view.file_dialog_open_table()
        if file == '':
            return

        success, msg = self.model.import_sequencing_table(file=file)
        if not success:
            self.view.message_box_error(msg=msg)

        self.view.refresh_table()


class ActionSaveClinicalDataTable(Action):

    def __call__(self):
        file = self.view.file_dialog_save_table(filename='clinical_data_table.csv')
        if file == '':
            return
        self.model.save_clinical_data_table(file=file)


class ActionSort(Action):

    ASCENDING: bool

    def __call__(self):
        columns = self.view.get_selected_columns()
        if len(columns) == 0:
            self.view.message_box_error(msg='Please select a column')
        elif len(columns) == 1:
            self.model.sort_dataframe(by=columns[0], ascending=self.ASCENDING)
            self.view.refresh_table()
        else:
            self.view.message_box_error(msg='Please select only one column')


class ActionSortAscending(ActionSort):

    ASCENDING = True


class ActionSortDescending(ActionSort):

    ASCENDING = False


class ActionDeleteSelectedRows(Action):

    def __call__(self):
        rows = self.view.get_selected_rows()
        if len(rows) == 0:
            return
        if self.view.message_box_yes_no(msg='Are you sure you want to delete the selected rows?'):
            self.model.drop(rows=rows)
            self.view.refresh_table()


class ActionResetTable(Action):

    def __call__(self):
        if len(self.model.dataframe) == 0:
            return  # nothing to reset

        if self.view.message_box_yes_no(msg='Are you sure you want to reset the table?'):
            self.model.reset_dataframe()
            self.view.refresh_table()


class ActionAddNewSample(Action):

    def __call__(self):
        attributes = self.view.dialog_edit_sample()

        if attributes is None:
            return

        self.model.append_row(attributes=attributes)
        self.view.refresh_table()


class ActionEditSample(Action):

    def __call__(self):
        rows = self.view.get_selected_rows()

        if len(rows) == 0:
            self.view.message_box_error(msg='Please select a row')
            return
        elif len(rows) > 1:
            self.view.message_box_error(msg='Please select only one row')
            return

        attributes = self.model.get_row(row=rows[0])
        attributes = self.view.dialog_edit_sample(attributes)

        if attributes is None:
            return

        self.model.update_row(row=rows[0], attributes=attributes)
        self.view.refresh_table()


class ActionExportCbioportalStudy(Action):

    def __call__(self):
        maf_dir = self.view.file_dialog_open_directory(caption='Select MAF directory')
        if maf_dir == '':
            return

        dstdir = self.view.file_dialog_open_directory(caption='Select destination directory')
        if dstdir == '':
            return

        try:
            study_info_dict = {
                'type_of_cancer': 'hnsc',
                'cancer_study_identifier': 'hnsc_nycu_2022',
                'name': 'Head and Neck Squamous Cell Carcinomas (NYCU, 2022)',
                'description': 'Whole exome sequencing of 11 precancer and OSCC tumor/normal pairs',
                'groups': 'PUBLIC',
                'reference_genome': 'hg38',
            }
            tags_dict = {'key': 'val'}

            self.model.export_cbioportal_study(
                maf_dir=maf_dir,
                study_info_dict=study_info_dict,
                tags_dict=tags_dict,
                dstdir=dstdir)
        except Exception as e:
            self.view.message_box_error(msg=str(e))
