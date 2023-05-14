from pydantic import BaseModel, Field, validator


class PeriodPredictionFeatureModel(BaseModel):
    Last: int = Field(...)
    Flow: int = Field(..., ge=1, le=5)
    Cramps: int = Field(..., ge=1, le=5)
    Mood: int = Field(..., ge=1, le=5)
    Ovulation: int = Field(..., ge=0, le=1)
    Age: int = Field(...)
    Weight: float = Field(...)
    Height: float = Field(...)
    BMI: float = Field(...)
    Race: str = Field(...)
    Medical_history: str = Field(...)
    Medications: str = Field(...)
    Length_of_menstrual_cycle: int = Field(...)
    Length_of_menses: int = Field(...)

    class Config:
        schema_extra = {
            "example": {

                "Last": 25,
                "Flow": 3,
                "Cramps": 3,
                "Mood": 2,
                "Ovulation": 1,
                "Age": 19,
                "Weight": 54,
                "Height": 163,
                "BMI": 20,
                "Race": "Native American",
                "Medical_history": "Nothing",
                "Medications": "Birth Control",
                "Length_of_menstrual_cycle": 29,
                "Length_of_menses": 6

            }
        }

    @validator("Race")
    def validate_race(cls, value):
        race = {'White': 4, 'Black': 1, 'Hispanic': 2, 'Asian': 0, 'Native American': 3}
        if value in race.keys():
            return race[value]
        else:
            raise ValueError("Incorrect Race Selected")

    @validator("Medical_history")
    def validate_medical_history(cls, value):
        medical_history = {'Nothing': 5, 'Asthma': 0, 'Diabetes': 2, 'Heart Disease': 4, 'Cancer': 1,
                           'Endometriosis': 3, 'PCOS': 6}
        if value in medical_history.keys():
            return medical_history[value]
        else:
            raise ValueError("Incorrect Medical History Selected")

    @validator("Medications")
    def validate_medications(cls, value):
        medications = {'Nothing': 2, 'Birth Control': 1, 'Pain Medication': 3, 'Antidepressants': 0}
        if value in medications.keys():
            return medications[value]
        else:
            raise ValueError("Incorrect Medication Selected")
