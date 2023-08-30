from enum import StrEnum

class GenderEnum(StrEnum):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

class CountryEnum(StrEnum):
    USA = 'usa'
    CANADA = 'canada'
    UK = 'uk'
    ISRAEL = 'israel'

class InterestsEnum(StrEnum):
    MUSIC = 'music'
    BOOKS = 'books'
    CHESS = 'chess'
    MOVIES = 'movies'    
