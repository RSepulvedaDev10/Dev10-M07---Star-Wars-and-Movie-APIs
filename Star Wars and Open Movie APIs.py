from dataclasses import dataclass, field
import datetime as dt
import requests
import json
import csv

@dataclass
class StarWarsFilms:
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: dt.date
    characters: list
    plot: str
    rotten_tomatoes: int
    box_office_gross: int = field(metadata={"units":"U.S dollars"})
    
    def __gt__(self, other):
        return self.episode_id > other.episode_id
    
    def __ge__(self, other):
        return self.episode_id >= other.episode_id


@dataclass
class StarWarsCharacter:
    name: str
    height: int = field(metadata={"units":"cenitmeters"})
    mass: int = field(metadata={"units":"kilograms"})
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
    
    