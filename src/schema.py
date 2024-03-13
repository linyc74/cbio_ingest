from typing import List, Dict, Any, Type
from .columns import *


NYCU_OSCC = 'NYCU OSCC'
TPVGH_LUAD = 'TPVGH LUAD'
TPVGH_HNSCC = 'TPVGH HNSCC'


class Schema:

    NAME: str

    DISPLAY_COLUMNS: List[str]

    AUTOGENERATED_COLUMNS: List[str]

    COLUMN_ATTRIBUTES: Dict[
        str, Dict[
            str, Any
        ]
    ]


class NycuOsccSchema(Schema):

    NAME = NYCU_OSCC

    DISPLAY_COLUMNS = [
        SAMPLE_ID,
        MEDICAL_RECORD_ID,
        PATHOLOGICAL_RECORD_ID,
        PATIENT_NAME,
        LAB_ID,
        LAB_SAMPLE_ID,
        SAMPLE_COLLECTION_DATE,
        SEX,
        PATIENT_WEIGHT,
        PATIENT_HEIGHT,
        ETHNICITY_CATEGORY,
        BIRTH_DATE,
        CLINICAL_DIAGNOSIS_DATE,
        CLINICAL_DIAGNOSIS_AGE,
        PATHOLOGICAL_DIAGNOSIS_DATE,
        CANCER_TYPE,
        CANCER_TYPE_DETAILED,
        SAMPLE_TYPE,
        ONCOTREE_CODE,
        SOMATIC_STATUS,
        CENTER,
        TUMOR_DISEASE_ANATOMIC_SITE,
        ICD_O_3_SITE_CODE,
        ALCOHOL_CONSUMPTION,
        ALCOHOL_CONSUMPTION_FREQUENCY,
        ALCOHOL_CONSUMPTION_DURATION,
        ALCOHOL_CONSUMPTION_QUIT,
        BETEL_NUT_CHEWING,
        BETEL_NUT_CHEWING_FREQUENCY,
        BETEL_NUT_CHEWING_DURATION,
        BETEL_NUT_CHEWING_QUIT,
        CIGARETTE_SMOKING,
        CIGARETTE_SMOKING_FREQUENCY,
        CIGARETTE_SMOKING_DURATION,
        CIGARETTE_SMOKING_QUIT,
        HISTOLOGIC_GRADE,
        SURGERY,
        NEOADJUVANT_INDUCTION_CHEMOTHERAPY,
        NEOADJUVANT_INDUCTION_CHEMOTHERAPY_DRUG,
        ADJUVANT_CHEMOTHERAPY,
        ADJUVANT_CHEMOTHERAPY_DRUG,
        PALLIATIVE_CHEMOTHERAPY,
        PALLIATIVE_CHEMOTHERAPY_DRUG,
        ADJUVANT_TARGETED_THERAPY,
        ADJUVANT_TARGETED_THERAPY_DRUG,
        PALLIATIVE_TARGETED_THERAPY,
        PALLIATIVE_TARGETED_THERAPY_DRUG,
        IMMUNOTHERAPY,
        IMMUNOTHERAPY_DRUG,
        RADIATION_THERAPY,
        RADIATION_THERAPY_DOSE,
        IHC_ANTI_PDL1_MAB_22C3_TPS,
        IHC_ANTI_PDL1_MAB_22C3_CPS,
        IHC_ANTI_PDL1_MAB_28_8_TPS,
        IHC_ANTI_PDL1_MAB_28_8_CPS,
        LYMPH_NODE_LEVEL_I,
        LYMPH_NODE_LEVEL_IA,
        LYMPH_NODE_LEVEL_IB,
        LYMPH_NODE_LEVEL_II,
        LYMPH_NODE_LEVEL_IIA,
        LYMPH_NODE_LEVEL_IIB,
        LYMPH_NODE_LEVEL_III,
        LYMPH_NODE_LEVEL_IV,
        LYMPH_NODE_LEVEL_V,
        LYMPH_NODE_RIGHT,
        LYMPH_NODE_LEFT,
        TOTAL_LYMPH_NODE,
        LYMPHOVASCULAR_INVASION,
        PERINEURAL_INVASION,
        CLINICAL_OVERT_EXTRANODAL_EXTENSION,
        PATHOLOGICAL_EXTRANODAL_EXTENSION,
        DEPTH_OF_INVASION,
        TUMOR_MARGIN,
        CLINICAL_TNM,
        PATHOLOGICAL_TNM,
        POSTNEOADJUVANT_CLINICAL_TNM,
        POSTNEOADJUVANT_PATHOLOGICAL_TNM,
        NEOPLASM_DISEASE_STAGE_AMERICAN_JOINT_COMMITTEE_ON_CANCER_CODE,
        ICD_10_CLASSIFICATION,
        SUBTYPE,
        INITIAL_TREATMENT_COMPLETION_DATE,
        LAST_FOLLOW_UP_DATE,
        RECUR_DATE_AFTER_INITIAL_TREATMENT,
        EXPIRE_DATE,
        CAUSE_OF_DEATH,
        DISEASE_FREE_SURVIVAL_MONTHS,
        DISEASE_FREE_SURVIVAL_STATUS,
        DISEASE_SPECIFIC_SURVIVAL_MONTHS,
        DISEASE_SPECIFIC_SURVIVAL_STATUS,
        OVERALL_SURVIVAL_MONTHS,
        OVERALL_SURVIVAL_STATUS,
    ]

    AUTOGENERATED_COLUMNS = [
        CLINICAL_DIAGNOSIS_AGE,
        ICD_O_3_SITE_CODE,
        ICD_10_CLASSIFICATION,
        LYMPH_NODE_LEVEL_I,
        LYMPH_NODE_LEVEL_II,
        TOTAL_LYMPH_NODE,
        NEOPLASM_DISEASE_STAGE_AMERICAN_JOINT_COMMITTEE_ON_CANCER_CODE,
        DISEASE_FREE_SURVIVAL_MONTHS,
        DISEASE_FREE_SURVIVAL_STATUS,
        DISEASE_SPECIFIC_SURVIVAL_MONTHS,
        DISEASE_SPECIFIC_SURVIVAL_STATUS,
        OVERALL_SURVIVAL_MONTHS,
        OVERALL_SURVIVAL_STATUS,
    ]

    COLUMN_ATTRIBUTES = {
        SAMPLE_ID: {
            'type': 'str',
            'options': ['000-00000-0000-E-X00-00'],
        },
        MEDICAL_RECORD_ID: {
            'type': 'str',
        },
        PATHOLOGICAL_RECORD_ID: {
            'type': 'str',
        },
        PATIENT_NAME: {
            'type': 'str',
        },
        LAB_ID: {
            'type': 'str',
            'options': ['XXX_LAB'],
        },
        LAB_SAMPLE_ID: {
            'type': 'str',
            'options': ['VGH_001_T', 'NYCUH_001_T'],
        },
        PATIENT_ID: {
            'type': 'str',
            'options': ['000-00000'],
        },
        SAMPLE_COLLECTION_DATE: {
            'type': 'date',
            'options': ['2020-01-01'],
        },
        SEX: {
            'type': 'str',
            'options': ['Male', 'Female'],
        },
        PATIENT_WEIGHT: {
            'type': 'float',
            'options': [0.0],
        },
        PATIENT_HEIGHT: {
            'type': 'float',
            'options': [0.0],
        },
        ETHNICITY_CATEGORY: {
            'type': 'str',
            'options': ['Han', 'Aboriginal'],
        },
        BIRTH_DATE: {
            'type': 'date',
            'options': ['1900-01-01'],
        },
        CLINICAL_DIAGNOSIS_DATE: {
            'type': 'date',
            'options': ['2020-01-01'],
        },
        PATHOLOGICAL_DIAGNOSIS_DATE: {
            'type': 'date',
            'options': ['2020-01-01'],
        },
        CLINICAL_DIAGNOSIS_AGE: {
            'type': 'float',
        },
        CANCER_TYPE: {
            'type': 'str',
            'options': ['Head and Neck Cancer'],
        },
        CANCER_TYPE_DETAILED: {
            'type': 'str',
            'options': ['Oral Cavity Squamous Cell Carcinoma', 'Head and Neck Squamous Cell Carcinoma'],
        },
        SAMPLE_TYPE: {
            'type': 'str',
            'options': ['Primary', 'Precancer', 'Recurrent'],
        },
        ONCOTREE_CODE: {
            'type': 'str',
            'options': ['OCSC', 'OPHSC'],
        },
        SOMATIC_STATUS: {
            'type': 'str',
            'options': ['Matched Adjacent Normal', 'Matched Blood Normal', 'Tumor Only'],
        },
        CENTER: {
            'type': 'str',
            'options': ['Taipei Veterans General Hospital', 'National Yang Ming Chiao Tung University Hospital'],
        },
        TUMOR_DISEASE_ANATOMIC_SITE: {
            'type': 'str',
            'options': [
                'Retromolar Triangle',
                'Right Tongue',
                'Left Tongue',
                'Cross Midline (CM) Tongue',
                'Left Upper Gingiva',
                'Left Lower Gingiva',
                'Right Upper Gingiva',
                'Right Lower Gingiva',
                'Cross Midline (CM) Left Upper Gingiva',
                'Cross Midline (CM) Right Lower Gingiva',
                'Cross Midline (CM) Gingiva',
                'Left Palate',
                'Right Palate',
                'Cross Midline (CM) Palate',
                'Upper Lip',
                'Lower Lip',
                'External Upper Lip',
                'External Lower Lip',
                'Upper Lip Inner Aspect',
                'Lower Lip Inner Aspect',
                'Cross Midline (CM) Lip',
                'Left Buccal Mucosa',
                'Right Buccal Mucosa',
            ],
        },
        ICD_O_3_SITE_CODE: {
            'type': 'str',
        },
        ALCOHOL_CONSUMPTION: {
            'type': 'str',
            'options': ['Current', 'Ex', 'Never'],
        },
        ALCOHOL_CONSUMPTION_FREQUENCY: {
            'type': 'str',
            'options': ['0.0', 'Occasional', 'Social'],
        },
        ALCOHOL_CONSUMPTION_DURATION: {
            'type': 'float',
            'options': [0.0],
        },
        ALCOHOL_CONSUMPTION_QUIT: {
            'type': 'float',
            'options': [0.0],
        },
        BETEL_NUT_CHEWING: {
            'type': 'str',
            'options': ['Current', 'Ex', 'Never'],
        },
        BETEL_NUT_CHEWING_FREQUENCY: {
            'type': 'str',
            'options': ['0.0', 'Occasional', 'Social'],
        },
        BETEL_NUT_CHEWING_DURATION: {
            'type': 'float',
            'options': [0.0],
        },
        BETEL_NUT_CHEWING_QUIT: {
            'type': 'float',
            'options': [0.0],
        },
        CIGARETTE_SMOKING: {
            'type': 'str',
            'options': ['Current', 'Ex', 'Never']
        },
        CIGARETTE_SMOKING_FREQUENCY: {
            'type': 'sting',
            'options': ['0.0', 'Occasional', 'Social'],
        },
        CIGARETTE_SMOKING_DURATION: {
            'type': 'float',
            'options': [0.0],
        },
        CIGARETTE_SMOKING_QUIT: {
            'type': 'float',
            'options': [0.0],
        },
        HISTOLOGIC_GRADE: {
            'type': 'str',
            'options': ['Well Differentiated', 'Moderately Differentiated', 'Poorly Differentiated',
                        'Undifferentated Anaplastic'],
        },
        SURGERY: {
            'type': 'str',
            'options': ['Wide Excision', 'Neck Dissection', 'Wide Excision and Neck Dissection'],
        },
        NEOADJUVANT_INDUCTION_CHEMOTHERAPY: {
            'type': 'bool',
            'options': [False, True],
        },
        NEOADJUVANT_INDUCTION_CHEMOTHERAPY_DRUG: {
            'type': 'str',
            'options': [
                '',
                'Cisplatin',
                '5-FU',
                'Docetaxel',
                'Cisplatin and 5-FU',
                'Docetaxel and Cisplatin',
                'Docetaxel, Cisplatin and 5-FU (TPF)',
                'Cisplatin, Mitomycin and 5-FU (PMU)',
            ],
        },
        ADJUVANT_CHEMOTHERAPY: {
            'type': 'bool',
            'options': [False, True],
        },
        ADJUVANT_CHEMOTHERAPY_DRUG: {
            'type': 'str',
            'options': [
                '',
                'Cisplatin',
                '5-FU',
                'Docetaxel',
                'Cisplatin and 5-FU',
                'Docetaxel and Cisplatin',
                'Docetaxel, Cisplatin and 5-FU (TPF)',
                'Cisplatin, Mitomycin and 5-FU (PMU)',
            ],
        },
        PALLIATIVE_CHEMOTHERAPY: {
            'type': 'bool',
            'options': [False, True],
        },
        PALLIATIVE_CHEMOTHERAPY_DRUG: {
            'type': 'str',
            'options': [
                '',
                'Cisplatin',
                '5-FU',
                'Docetaxel',
                'Cisplatin and 5-FU',
                'Docetaxel and Cisplatin',
                'Docetaxel, Cisplatin and 5-FU (TPF)',
                'Cisplatin, Mitomycin and 5-FU (PMU)',
            ],
        },
        ADJUVANT_TARGETED_THERAPY: {
            'type': 'bool',
            'options': [False, True],
        },
        ADJUVANT_TARGETED_THERAPY_DRUG: {
            'type': 'str',
            'options': [
                '',
                'Cetuximab',
                'Cetuximab and Docetaxel',
            ],
        },
        PALLIATIVE_TARGETED_THERAPY: {
            'type': 'bool',
            'options': [False, True],
        },
        PALLIATIVE_TARGETED_THERAPY_DRUG: {
            'type': 'str',
            'options': [
                '',
                'Cetuximab',
                'Cetuximab and Docetaxel',
            ],
        },
        IMMUNOTHERAPY: {
            'type': 'bool',
            'options': [False, True],
        },
        IMMUNOTHERAPY_DRUG: {
            'type': 'str',
            'options': ['', 'Pembrolizumab', 'Nivolumab'],
        },
        RADIATION_THERAPY: {
            'type': 'str',
            'options': ['Definitive', 'Adjuvant', 'Palliative'],
        },
        RADIATION_THERAPY_DOSE: {
            'type': 'float',
            'options': [0.0],
        },
        IHC_ANTI_PDL1_MAB_22C3_TPS: {
            'type': 'str',
            'options': ['> 50%', '< 50%'],
        },
        IHC_ANTI_PDL1_MAB_22C3_CPS: {
            'type': 'str',
            'options': ['> 50%', '< 50%'],
        },
        IHC_ANTI_PDL1_MAB_28_8_TPS: {
            'type': 'str',
            'options': ['> 50%', '< 50%'],
        },
        IHC_ANTI_PDL1_MAB_28_8_CPS: {
            'type': 'str',
            'options': ['> 50%', '< 50%'],
        },
        LYMPH_NODE_LEVEL_I: {
            'type': 'str',
            'options': ['0/0', ''],
        },
        LYMPH_NODE_LEVEL_IA: {
            'type': 'str',
            'options': ['0/0', ''],
        },
        LYMPH_NODE_LEVEL_IB: {
            'type': 'str',
            'options': ['0/0', ''],
        },
        LYMPH_NODE_LEVEL_II: {
            'type': 'str',
            'options': ['0/0', ''],
        },
        LYMPH_NODE_LEVEL_IIA: {
            'type': 'str',
            'options': ['0/0', ''],
        },
        LYMPH_NODE_LEVEL_IIB: {
            'type': 'str',
            'options': ['0/0', ''],
        },
        LYMPH_NODE_LEVEL_III: {
            'type': 'str',
            'options': ['0/0', ''],
        },
        LYMPH_NODE_LEVEL_IV: {
            'type': 'str',
            'options': ['0/0', ''],
        },
        LYMPH_NODE_LEVEL_V: {
            'type': 'str',
            'options': ['0/0', ''],
        },
        LYMPH_NODE_RIGHT: {
            'type': 'str',
            'options': ['0/0', ''],
        },
        LYMPH_NODE_LEFT: {
            'type': 'str',
            'options': ['0/0', ''],
        },
        TOTAL_LYMPH_NODE: {
            'type': 'str',
            'options': ['0/0', ''],
        },
        LYMPHOVASCULAR_INVASION: {
            'type': 'bool',
            'options': [False, True],
        },
        PERINEURAL_INVASION: {
            'type': 'str',
            'options': ['Negative', 'Positive', 'Extensive'],
        },
        CLINICAL_OVERT_EXTRANODAL_EXTENSION: {
            'type': 'bool',
            'options': [False, True],
        },
        PATHOLOGICAL_EXTRANODAL_EXTENSION: {
            'type': 'str',
            'options': ['Negative', 'Micro', 'Macro'],
        },
        DEPTH_OF_INVASION: {
            'type': 'float',
            'options': [0.0],
        },
        TUMOR_MARGIN: {
            'type': 'str',
            'options': ['Negative (> 4mm)', 'Negative (> 4mm) with dysplasia', 'Close (≤ 4mm)', 'Close (≤ 4mm)  with dysplasia', 'Positive'],
        },
        CLINICAL_TNM: {
            'type': 'str',
            'options': [
                'T1N0M0',
                'TisN0M0',
                'T2N0M0',
                'T3N0M0',
                'T1N1M0',
                'T2N1M0',
                'T3N1M0',
                'T4aN0M0',
                'T4aN1M0',
                'T1N2M0',
                'T2N2M0',
                'T3N2M0',
                'T4aN2M0',
                'T1N3M0',
                'T2N3M0',
                'T3N3M0',
                'T4aN3M0',
                'T4bN0M0',
                'T4bN1M0',
                'T4bN2M0',
                'T4bN3M0',
                'T4bN3M1',
            ],
        },
        PATHOLOGICAL_TNM: {
            'type': 'str',
            'options': [
                'T1N0M0',
                'TisN0M0',
                'T2N0M0',
                'T3N0M0',
                'T1N1M0',
                'T2N1M0',
                'T3N1M0',
                'T4aN0M0',
                'T4aN1M0',
                'T1N2M0',
                'T2N2M0',
                'T3N2M0',
                'T4aN2M0',
                'T1N3M0',
                'T2N3M0',
                'T3N3M0',
                'T4aN3M0',
                'T4bN0M0',
                'T4bN1M0',
                'T4bN2M0',
                'T4bN3M0',
                'T4bN3M1',
            ],
        },
        POSTNEOADJUVANT_CLINICAL_TNM: {
            'type': 'str',
            'options': [
                '',
                'T1N0M0',
                'TisN0M0',
                'T2N0M0',
                'T3N0M0',
                'T1N1M0',
                'T2N1M0',
                'T3N1M0',
                'T4aN0M0',
                'T4aN1M0',
                'T1N2M0',
                'T2N2M0',
                'T3N2M0',
                'T4aN2M0',
                'T1N3M0',
                'T2N3M0',
                'T3N3M0',
                'T4aN3M0',
                'T4bN0M0',
                'T4bN1M0',
                'T4bN2M0',
                'T4bN3M0',
                'T4bN3M1',
            ],
        },
        POSTNEOADJUVANT_PATHOLOGICAL_TNM: {
            'type': 'str',
            'options': [
                '',
                'T1N0M0',
                'TisN0M0',
                'T2N0M0',
                'T3N0M0',
                'T1N1M0',
                'T2N1M0',
                'T3N1M0',
                'T4aN0M0',
                'T4aN1M0',
                'T1N2M0',
                'T2N2M0',
                'T3N2M0',
                'T4aN2M0',
                'T1N3M0',
                'T2N3M0',
                'T3N3M0',
                'T4aN3M0',
                'T4bN0M0',
                'T4bN1M0',
                'T4bN2M0',
                'T4bN3M0',
                'T4bN3M1',
            ],
        },
        NEOPLASM_DISEASE_STAGE_AMERICAN_JOINT_COMMITTEE_ON_CANCER_CODE: {
            'type': 'str',
            'options': ['Stage I', 'Stage II', 'Stage III', 'Stage IVA', 'Stage IVB', 'Stage IVC'],
        },
        ICD_10_CLASSIFICATION: {
            'type': 'str',
        },
        SUBTYPE: {
            'type': 'str',
            'options': ['HNSC HPV-', 'HNSC HPV+', ''],
        },
        INITIAL_TREATMENT_COMPLETION_DATE: {
            'type': 'date',
            'options': ['2020-01-01'],
        },
        LAST_FOLLOW_UP_DATE: {
            'type': 'date',
            'options': ['2020-01-01'],
        },
        RECUR_DATE_AFTER_INITIAL_TREATMENT: {
            'type': 'date',
            'options': ['', '2020-01-01'],
        },
        EXPIRE_DATE: {
            'type': 'date',
            'options': ['', '2020-01-01'],
        },
        CAUSE_OF_DEATH: {
            'type': 'str',
            'options': ['Cancer', 'Other Disease', 'Other Cancer'],
        },
        DISEASE_FREE_SURVIVAL_MONTHS: {
            'type': 'float',
        },
        DISEASE_FREE_SURVIVAL_STATUS: {
            'type': 'str',
            'options': ['0:DiseaseFree', '1:Recurred/Progressed'],
        },
        DISEASE_SPECIFIC_SURVIVAL_MONTHS: {
            'type': 'float',
        },
        DISEASE_SPECIFIC_SURVIVAL_STATUS: {
            'type': 'str',
            'options': ['0:ALIVE OR DEAD TUMOR FREE', '1:DEAD WITH TUMOR'],
        },
        OVERALL_SURVIVAL_MONTHS: {
            'type': 'float',
        },
        OVERALL_SURVIVAL_STATUS: {
            'type': 'str',
            'options': ['0:LIVING', '1:DECEASED'],
        },
    }


class TpvghLuadSchema(Schema):

    NAME = TPVGH_LUAD

    DISPLAY_COLUMNS = [
        SERIAL_NO,
        GENDER,
        BIRTHDATE,
        AGE,
        SMOKING,
        SMOKING_AMOUNT_PPD,
        SMOKING_YEARS,
        QUIT_SMOKING_YEARS,
        LUNG_CANCER_FAMILY_HISTORY,
        NEOADJUVANT_THERAPY,
        NEOADJUVANT_THERAPY_START_DATE,
        NEOADJUVANT_THERAPY_END_DATE,
        ADJUVANT_THERAPY,
        ADJUVANT_THERAPY_START_DATE,
        ADJUVANT_THERAPY_END_DATE,
        LAST_F_U_DATE,
        DFS,
        DEATH,
        DEATH_DATE,
        OS,
        HISTOLOGIC_TYPE,
        SUBTYPE_FOR_INVASIVE_NONMUCINOUS_ADENOCARCINOMA,
        HISTOLOGIC_GRADE,
        SPREAD_THROUGH_AIR_SPACES,
        VISCERAL_PLEURA_INVASION,
        LYMPHOVASCULAR_INVASION,
        PRIMARY_TUMOR,
        REGIONAL_LYMPH_NODES,
        DISTANT_METASTASIS,
    ]

    AUTOGENERATED_COLUMNS = []

    COLUMN_ATTRIBUTES = {
        SERIAL_NO: {
            'type': 'str',
            'options': ['C0000'],
        },
        GENDER: {
            'type': 'str',
            'options': ['F', 'M'],
        },
        BIRTHDATE: {
            'type': 'date',
            'options': ['1900-01-01'],
        },
        AGE: {
            'type': 'int',
        },
        SMOKING: {
            'type': 'int',
            'options': [0, 1],
        },
        SMOKING_AMOUNT_PPD: {
            'type': 'float',
        },
        SMOKING_YEARS: {
            'type': 'float',
        },
        QUIT_SMOKING_YEARS: {
            'type': 'float',
        },
        LUNG_CANCER_FAMILY_HISTORY: {
            'type': 'str',
            'options': ['None', 'Mother', 'Father'],
        },
        NEOADJUVANT_THERAPY: {
            'type': 'str',
            'options': [
                '-',
                'Tegafur',
            ],
        },
        NEOADJUVANT_THERAPY_START_DATE: {
            'type': 'date_list',
            'options': ['', '2020-01-01'],
        },
        NEOADJUVANT_THERAPY_END_DATE: {
            'type': 'date_list',
            'options': ['', '2020-01-01'],
        },
        ADJUVANT_THERAPY: {
            'type': 'str',
            'options': [
                '-',
                'Tegafur',
                'Tegafur, Erlotinib',
                'Vinorelbine, Cisplatin'
                'Vinorelbine, Cisplatin, Afatinib',
                'Vinorelbine, Carboplatin',
            ],
        },
        ADJUVANT_THERAPY_START_DATE: {
            'type': 'date_list',
            'options': ['', '2020-01-01'],
        },
        ADJUVANT_THERAPY_END_DATE: {
            'type': 'date_list',
            'options': ['', '2020-01-01'],
        },
        LAST_F_U_DATE: {
            'type': 'str',
            'options': ['2020-01-01'],
        },
        DFS: {
            'type': 'float',
        },
        DEATH: {
            'type': 'bool',
            'options': [False, True],
        },
        DEATH_DATE: {
            'type': 'date',
            'options': ['', '2020-01-01'],
        },
        OS: {
            'type': 'float',
        },
        HISTOLOGIC_TYPE: {
            'type': 'str',
            'options': [
                'Invasive adenocarcinoma, nonmucinous',
                'Invasive squamous cell carcinoma, non-keratinizing',
                'Invasive squamous cell carcinoma, keratinizing',
                'Minimally invasive adenocarcinoma, nonmucinous',
                'Adenosquamous carcinoma',
            ],
        },
        SUBTYPE_FOR_INVASIVE_NONMUCINOUS_ADENOCARCINOMA: {
            'type': 'str',
            'options': ['Acinar', 'Micropapillary', 'Lepidic', 'Solid', 'Papillary'],
        },
        HISTOLOGIC_GRADE: {
            'type': 'str',
            'options': ['G1: Well differentiated', 'G2: Moderately differentiated', 'G3: Poorly differentiated', 'Not applicable'],
        },
        SPREAD_THROUGH_AIR_SPACES: {
            'type': 'str',
            'options': ['Not identified', 'Present'],
        },
        VISCERAL_PLEURA_INVASION: {
            'type': 'str',
            'options': ['Not identified', 'Present (PL1)', 'Present (PL2)'],
        },
        LYMPHOVASCULAR_INVASION: {
            'type': 'str',
            'options': ['Not identified', 'Present'],
        },
        PRIMARY_TUMOR: {
            'type': 'str',
            'options': ['pT1mi', 'pT1a', 'pT1b', 'pT2a', 'pT2b', 'pT3'],
        },
        REGIONAL_LYMPH_NODES: {
            'type': 'str',
            'options': ['pN0', 'pN1', 'pN2', 'pNX'],
        },
        DISTANT_METASTASIS: {
            'type': 'str',
            'options': ['No distant metastasis in specimen examined'],
        },
    }


class TpvghHnsccSchema(Schema):

    NAME = TPVGH_HNSCC

    DISPLAY_COLUMNS = [
        SAMPLE_ID,
        MEDICAL_RECORD_ID,
        PATHOLOGICAL_RECORD_ID,
        PATIENT_NAME,
        LAB_ID,
        LAB_SAMPLE_ID,
        BIRTH_DATE,
        CLINICAL_DIAGNOSIS_DATE,
        CLINICAL_DIAGNOSIS_AGE,
        INITIAL_TREATMENT_COMPLETION_DATE,
        LAST_FOLLOW_UP_DATE,
        RECUR_DATE_AFTER_INITIAL_TREATMENT,
        EXPIRE_DATE,
        CAUSE_OF_DEATH,
        DISEASE_FREE_SURVIVAL_MONTHS,
        DISEASE_FREE_SURVIVAL_STATUS,
        DISEASE_SPECIFIC_SURVIVAL_MONTHS,
        DISEASE_SPECIFIC_SURVIVAL_STATUS,
        OVERALL_SURVIVAL_MONTHS,
        OVERALL_SURVIVAL_STATUS,
    ]

    AUTOGENERATED_COLUMNS = [
        CLINICAL_DIAGNOSIS_AGE,
        DISEASE_FREE_SURVIVAL_MONTHS,
        DISEASE_FREE_SURVIVAL_STATUS,
        DISEASE_SPECIFIC_SURVIVAL_MONTHS,
        DISEASE_SPECIFIC_SURVIVAL_STATUS,
        OVERALL_SURVIVAL_MONTHS,
        OVERALL_SURVIVAL_STATUS,
    ]

    COLUMN_ATTRIBUTES = {
        SAMPLE_ID: {
            'type': 'str',
            'options': ['000-00000-0000-E-X00-00'],
        },
        MEDICAL_RECORD_ID: {
            'type': 'str',
        },
        PATHOLOGICAL_RECORD_ID: {
            'type': 'str',
        },
        PATIENT_NAME: {
            'type': 'str',
        },
        LAB_ID: {
            'type': 'str',
            'options': ['XXX_LAB'],
        },
        LAB_SAMPLE_ID: {
            'type': 'str',
            'options': ['VGH_001_T', 'NYCUH_001_T'],
        },
        BIRTH_DATE: {
            'type': 'date',
            'options': ['1900-01-01'],
        },
        CLINICAL_DIAGNOSIS_DATE: {
            'type': 'date',
            'options': ['2020-01-01'],
        },
        CLINICAL_DIAGNOSIS_AGE: {
            'type': 'float',
        },
        INITIAL_TREATMENT_COMPLETION_DATE: {
            'type': 'date',
            'options': ['2020-01-01'],
        },
        LAST_FOLLOW_UP_DATE: {
            'type': 'date',
            'options': ['2020-01-01'],
        },
        RECUR_DATE_AFTER_INITIAL_TREATMENT: {
            'type': 'date',
            'options': ['', '2020-01-01'],
        },
        EXPIRE_DATE: {
            'type': 'date',
            'options': ['', '2020-01-01'],
        },
        CAUSE_OF_DEATH: {
            'type': 'str',
            'options': ['Cancer', 'Other Disease', 'Other Cancer'],
        },
        DISEASE_FREE_SURVIVAL_MONTHS: {
            'type': 'float',
        },
        DISEASE_FREE_SURVIVAL_STATUS: {
            'type': 'str',
            'options': ['0:DiseaseFree', '1:Recurred/Progressed'],
        },
        DISEASE_SPECIFIC_SURVIVAL_MONTHS: {
            'type': 'float',
        },
        DISEASE_SPECIFIC_SURVIVAL_STATUS: {
            'type': 'str',
            'options': ['0:ALIVE OR DEAD TUMOR FREE', '1:DEAD WITH TUMOR'],
        },
        OVERALL_SURVIVAL_MONTHS: {
            'type': 'float',
        },
        OVERALL_SURVIVAL_STATUS: {
            'type': 'str',
            'options': ['0:LIVING', '1:DECEASED'],
        },
    }


DATA_SCHEMA_DICT: Dict[str, Type[Schema]] = {
    NYCU_OSCC: NycuOsccSchema,
    TPVGH_LUAD: TpvghLuadSchema,
    TPVGH_HNSCC: TpvghHnsccSchema,
}
