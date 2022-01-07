from dataclasses import dataclass, fields
import datetime as dt
import requests

@dataclass
class StarWarsFilms:
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: dt.date
    characters: list


@dataclass
class StarWarsCharacter:
    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    

@dataclass  
class StarWarsLibrary(StarWarsFilms):
    movies: list
    shows: list
    last_updated: dt.date