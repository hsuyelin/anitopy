# -*- coding: utf-8 -*-

from enum import Enum


class ElementCategory(Enum):
    ANIME_SEASON = 'anime_season'
    ANIME_SEASON_PREFIX = 'anime_season_prefix'
    ANIME_TITLE = 'anime_title'
    ANIME_TYPE = 'anime_type'
    ANIME_YEAR = 'anime_year'
    AUDIO_TERM = 'audio_term'
    DEVICE_COMPATIBILITY = 'device_compatibility'
    EPISODE_NUMBER = 'episode_number'
    EPISODE_NUMBER_ALT = 'episode_number_alt'
    EPISODE_PREFIX = 'episode_prefix'
    EPISODE_TITLE = 'episode_title'
    FILE_CHECKSUM = 'file_checksum'
    FILE_EXTENSION = 'file_extension'
    FILE_NAME = 'file_name'
    LANGUAGE = 'language'
    OTHER = 'other'
    RELEASE_GROUP = 'release_group'
    RELEASE_INFORMATION = 'release_information'
    RELEASE_VERSION = 'release_version'
    SOURCE = 'source'
    SUBTITLES = 'subtitles'
    VIDEO_RESOLUTION = 'video_resolution'
    VIDEO_TERM = 'video_term'
    VOLUME_NUMBER = 'volume_number'
    VOLUME_PREFIX = 'volume_prefix'
    UNKNOWN = 'unknown'

    @classmethod
    def is_searchable(cls, category):
        searchable_categories = [
            cls.ANIME_SEASON_PREFIX,
            cls.ANIME_TYPE,
            cls.AUDIO_TERM,
            cls.DEVICE_COMPATIBILITY,
            cls.EPISODE_PREFIX,
            cls.FILE_CHECKSUM,
            cls.LANGUAGE,
            cls.OTHER,
            cls.RELEASE_GROUP,
            cls.RELEASE_INFORMATION,
            cls.RELEASE_VERSION,
            cls.SOURCE,
            cls.SUBTITLES,
            cls.VIDEO_RESOLUTION,
            cls.VIDEO_TERM,
            cls.VOLUME_PREFIX
        ]
        return category in searchable_categories

    @classmethod
    def is_singular(cls, category):
        non_singular_categories = [
            cls.ANIME_SEASON,
            cls.ANIME_TYPE,
            cls.AUDIO_TERM,
            cls.DEVICE_COMPATIBILITY,
            cls.EPISODE_NUMBER,
            cls.LANGUAGE,
            cls.OTHER,
            cls.RELEASE_INFORMATION,
            cls.SOURCE,
            cls.VIDEO_TERM
        ]
        return category not in non_singular_categories


class Elements:
    def __init__(self):
        self._elements = {}

    def insert(self, category, content):
        self._elements.setdefault(category, []).append(content)

    def contains(self, category):
        return bool(category in self._elements.keys() and
                    self._elements[category])

    def get_dictionary(self):
        return self._elements