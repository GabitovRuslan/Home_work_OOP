class Track:
    info_track = []

    def __init__(self, name_track, duration):
        self.name_track = name_track
        self.duration = duration

    def show(self):
        return f'{self.name_track} - {self.duration} мин.'


class Album:
    def __init__(self, name_album, group):
        self.name_album = name_album
        self.group = group
        self.track_list = []

    def add_tracks(self, x):
        self.track_list.append(x)

    def get_tracks(self):
        print(f'Название альбома: {self.name_album}\nИсполнитель: {self.group}')
        for x in self.track_list:
            print(x.show())

    def get_duration(self):
        max_time = sum(x.duration for x in self.track_list)
        print(f'Общая длина всех треков {max_time}')


track1 = Track('фантазер', 3)
track2 = Track('"Фан"', 5)
track3 = Track('"Буум>"', 5)
track4 = Track('фантазер', 8)
track5 = Track('"Фан"', 7)
track6 = Track('"Буум>"', 6)
album_apple = Album('Яблоко', 'На-на')
album_one = Album('Один', 'ДДТ')
album_apple.add_tracks(track1)
album_apple.add_tracks(track2)
album_apple.add_tracks(track3)
album_one.add_tracks(track4)
album_one.add_tracks(track5)
album_one.add_tracks(track6)
album_apple.get_tracks()
album_apple.get_duration()
album_one.get_tracks()
album_one.get_duration()
