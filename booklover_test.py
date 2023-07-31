import unittest
import booklover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        reader = booklover("Rick", "Rick@gmail.com", "Dictionaries", 1)
        reader.add_book("Oxford's English Dictionary", 4)
        book = reader.book_list["book_name"][0]
        rating = reader.book_list["rating"][0]
        both = [book, rating]
        self.assertEqual(both, ["Oxford's English Dictionary", 4])
        
        
    def test_2_add_book(self):
        reader = booklover("Rick", "Rick@gmail.com", "Dictionaries", 1)
        reader.add_book("Oxford's English Dictionary", 4)
        reader.add_book("Oxford's English Dictionary", 4)
        self.assertEqual(reader.book_list.value_counts()[0], 1)
    
    def test_3_has_read(self):
        reader = booklover("Rick", "Rick@gmail.com", "Dictionaries", 1)
        reader.add_book("Oxford's English Dictionary", 4)
        self.assertEqual(reader.has_read("Oxford's English Dictionary"), True)
        
    def test_4_has_read(self):
        reader = booklover("Rick", "Rick@gmail.com", "Dictionaries", 1)
        reader.add_book("Oxford's English Dictionary", 4)
        self.assertFalse(reader.has_read("Thesaurus"))
        
    def test_5_num_books_read(self):
        reader = booklover("Rick", "Rick@gmail.com", "Dictionaries", 1)
        reader.add_book("Oxford's English Dictionary", 4)
        reader.add_book("Thesaurus", 2)
        self.assertEqual(reader.num_books, 2)
        
    def test_6_fav_books(self):
        reader = booklover("Rick", "Rick@gmail.com", "Dictionaries", 1)
        reader.add_book("Thesaurus", 2)
        reader.add_book("Oxford's English Dictionary", 4)
        # If it is working properly then only oxford will be there
        # or else thesaurus will be there
        self.assertEqual(reader.fav_books()["rating"][0] > 3, True)
        
if __name__ == '__main__':

    unittest.main(verbosity=3)
