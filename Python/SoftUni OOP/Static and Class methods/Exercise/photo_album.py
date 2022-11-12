from math import ceil


class PhotoAlbum:

    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for index, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        separator = '-' * 11 + '\n'
        message = separator
        for page in self.photos:
            message += ' '.join('[]' for _ in page) + '\n' + separator
        return message.strip()
