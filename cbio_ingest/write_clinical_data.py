import pandas as pd
from typing import Dict, List
from .template import Processor
from .schema import STUDY_IDENTIFIER_KEY


class WriteClinicalData(Processor):

    study_info_dict: Dict[str, str]
    patient_df: pd.DataFrame
    sample_df: pd.DataFrame

    def main(
            self,
            study_info_dict: Dict[str, str],
            patient_df: pd.DataFrame,
            sample_df: pd.DataFrame):

        self.study_info_dict = study_info_dict
        self.patient_df = patient_df
        self.sample_df = sample_df

        WritePatientData(self.settings).main(
            patient_df=self.patient_df,
            study_info_dict=self.study_info_dict)

        WriteSampleData(self.settings).main(
            sample_df=self.sample_df,
            study_info_dict=self.study_info_dict)


class BaseWriter(Processor):

    DATA_FNAME: str

    df: pd.DataFrame
    study_info_dict: Dict[str, str]

    def write_data_file_1st_2nd_lines(self):
        line = '#' + '\t'.join(self.df.columns) + '\n'
        with open(f'{self.outdir}/{self.DATA_FNAME}', 'w') as fh:
            for _ in range(2):
                fh.write(line)

    def write_data_file_3rd_line(self):
        datatypes = GetDataTypes(self.settings).main(
            columns=self.df.columns.to_list()
        )

        line = '#' + '\t'.join(datatypes) + '\n'
        with open(f'{self.outdir}/{self.DATA_FNAME}', 'a') as fh:
            fh.write(line)

    def write_data_file_4th_line(self):
        items = ['1' for _ in self.df.columns]
        line = '#' + '\t'.join(items) + '\n'
        with open(f'{self.outdir}/{self.DATA_FNAME}', 'a') as fh:
            fh.write(line)


class WritePatientData(BaseWriter):

    META_FNAME = 'meta_clinical_patient.txt'
    DATA_FNAME = 'data_clinical_patient.txt'
    BOOLEAN_COLUMNS = [
        'Neoadjuvant/Induction Chemotherapy',
        'Adjuvant Chemotherapy',
        'Palliative Chemotherapy',
        'Adjuvant Targeted Therapy',
        'Palliative Targeted Therapy',
        'Immunotherapy',
        'Lymphovascular Invasion (LVI)',
        'Clinical Overt Extranodal Extension',
    ]
    KEYWORDS_FOR_NUMBER_DATATYPE = [
        '(Kg)', '(mm)', '(Years)', '(Months)', 'Frequency',
        'IHC Anti-PDL1',
    ]

    def main(
            self,
            patient_df: pd.DataFrame,
            study_info_dict: Dict[str, str]):

        self.df = patient_df
        self.study_info_dict = study_info_dict

        self.write_meta_file()
        self.write_data_file_1st_2nd_lines()
        self.write_data_file_3rd_line()
        self.write_data_file_4th_line()
        self.write_data_file()

    def write_meta_file(self):
        text = f'''\
cancer_study_identifier: {self.study_info_dict[STUDY_IDENTIFIER_KEY]}
genetic_alteration_type: CLINICAL
datatype: PATIENT_ATTRIBUTES
data_filename: {self.DATA_FNAME}'''

        with open(f'{self.outdir}/{self.META_FNAME}', 'w') as fh:
            fh.write(text)

    def write_data_file(self):
        self.df = FillInMissingBooleanValues(self.settings).main(self.df)
        self.df = FormatClinicalData(self.settings).main(self.df)
        self.df.to_csv(f'{self.outdir}/{self.DATA_FNAME}', mode='a', sep='\t', index=False)


class WriteSampleData(BaseWriter):

    META_FNAME = 'meta_clinical_sample.txt'
    DATA_FNAME = 'data_clinical_sample.txt'
    BOOLEAN_COLUMNS = [
        'Neoadjuvant/Induction Chemotherapy',
        'Adjuvant Chemotherapy',
        'Palliative Chemotherapy',
        'Adjuvant Targeted Therapy',
        'Palliative Targeted Therapy',
        'Immunotherapy',
        'Lymphovascular Invasion (LVI)',
        'Clinical Overt Extranodal Extension',
    ]
    KEYWORDS_FOR_NUMBER_DATATYPE = [
        '(Kg)', '(mm)', '(Years)', '(Months)', 'Frequency',
        'IHC Anti-PDL1',
    ]

    def main(
            self,
            sample_df: pd.DataFrame,
            study_info_dict: Dict[str, str]):

        self.df = sample_df
        self.study_info_dict = study_info_dict

        self.write_meta_file()
        self.write_data_file_1st_2nd_lines()
        self.write_data_file_3rd_line()
        self.write_data_file_4th_line()
        self.write_data_file()

    def write_meta_file(self):
        text = f'''\
cancer_study_identifier: {self.study_info_dict[STUDY_IDENTIFIER_KEY]}
genetic_alteration_type: CLINICAL
datatype: SAMPLE_ATTRIBUTES
data_filename: {self.DATA_FNAME}'''

        with open(f'{self.outdir}/{self.META_FNAME}', 'w') as fh:
            fh.write(text)

    def write_data_file(self):
        self.df = FillInMissingBooleanValues(self.settings).main(self.df)
        self.df = FormatClinicalData(self.settings).main(self.df)
        self.df.to_csv(f'{self.outdir}/{self.DATA_FNAME}', mode='a', sep='\t', index=False)


class FillInMissingBooleanValues(Processor):

    df: pd.DataFrame

    datatypes: List[str]

    def main(self, df: pd.DataFrame) -> pd.DataFrame:
        self.df = df

        self.set_datatypes()
        self.fillna()

        return self.df

    def set_datatypes(self):
        self.datatypes = GetDataTypes(self.settings).main(columns=self.df.columns.to_list())

    def fillna(self):
        for dtype, column in zip(self.datatypes, self.df.columns):
            if dtype == 'BOOLEAN':
                self.df[column] = self.df[column].fillna(value=False)


class GetDataTypes(Processor):

    BOOLEAN_COLUMNS = [
        'Neoadjuvant/Induction Chemotherapy',
        'Adjuvant Chemotherapy',
        'Palliative Chemotherapy',
        'Adjuvant Targeted Therapy',
        'Palliative Targeted Therapy',
        'Immunotherapy',
        'Lymphovascular Invasion (LVI)',
        'Clinical Overt Extranodal Extension',
    ]
    KEYWORDS_FOR_NUMBER_DATATYPE = [
        '(Kg)', '(mm)', '(Years)', '(Months)', 'Frequency',
    ]

    columns: List[str]

    datatypes: List[str]

    def main(self, columns: List[str]) -> List[str]:
        self.columns = columns

        self.datatypes = []
        for c in self.columns:
            dtype = 'STRING'
            if c in self.BOOLEAN_COLUMNS:
                dtype = 'BOOLEAN'
            for k in self.KEYWORDS_FOR_NUMBER_DATATYPE:
                if k in c:
                    dtype = 'NUMBER'
                    break
            self.datatypes.append(dtype)

        return self.datatypes


class FormatClinicalData(Processor):

    RENAME_COLUMN_DICT = {
        'DISEASE_FREE_SURVIVAL_MONTHS': 'DFS_MONTHS',
        'DISEASE_FREE_SURVIVAL_STATUS': 'DFS_STATUS',
        'DISEASE_SPECIFIC_SURVIVAL_MONTHS': 'DSS_MONTHS',
        'DISEASE_SPECIFIC_SURVIVAL_STATUS': 'DSS_STATUS',
        'OVERALL_SURVIVAL_MONTHS': 'OS_MONTHS',
        'OVERALL_SURVIVAL_STATUS': 'OS_STATUS',
        'PROGRESSION_FREE_SURVIVAL_MONTHS': 'PFS_MONTHS',
        'PROGRESSION_FREE_SURVIVAL_STATUS': 'PFS_STATUS',
    }
    REPLACE_VALUE_DICT = {
        True: 'TRUE',
        False: 'FALSE'
    }

    df: pd.DataFrame

    def main(self, df: pd.DataFrame) -> pd.DataFrame:
        self.df = df

        self.format_columns()
        self.rename_columns()
        self.replace_values()

        return self.df

    def format_columns(self):
        rename_dict = {c: self.__format(c) for c in self.df.columns}
        self.df = self.df.rename(columns=rename_dict)

    def __format(self, c: str) -> str:
        for x in [' ', '-', ',', '/']:
            c = c.upper().replace(x, '_')

        for x in ['(', ')']:
            c = c.replace(x, '')

        return c

    def rename_columns(self):
        self.df = self.df.rename(columns=self.RENAME_COLUMN_DICT)

    def replace_values(self):
        self.df = self.df.replace(to_replace=self.REPLACE_VALUE_DICT)
