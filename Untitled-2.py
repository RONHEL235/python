#Thursday [08:47]
# 06 March 2025 

# files/manipulation.py
from collections import Counter
from string import ascii_letters
chars = ascii_letters + ' '

def sanitize(s, chars):
 return ''.join(c for c in s if c in chars)
def reverse(s):
 return s[::-1]
with open('fear.txt') as stream:
 lines = [line.rstrip() for line in stream]
# let's write the mirrored version of the file
with open('raef.txt', 'w') as stream:
 stream.write('\n'.join(reverse(line) for line in lines))
# now we can calculate some statistics
lines = [sanitize(line, chars) for line in lines]
whole = ' '.join(lines)
# we perform comparisons on the lowercased version of 'whole'
cnt = Counter(whole.lower().split())
# we can print the N most common words
print(cnt.most_common(3))

#The rstrip()

text = "Hello, World!   "
clean_text = text.lstrip()
print(f"'{clean_text}'")  # Output: 'Hello, World!'

#Working with File and Directories 

# files/walking.py
import os
for root, dirs, files in os.walk('.'):
    abs_root = os.path.abspath(root)
    print(abs_root)

    if dirs:
        print('Directories:')

    for dir_ in dirs:
      print(dir_)

    print()
    if files:
        print('Files:')
    for filename in files:
        print(filename)
    print()

#Database Programming

# persistence/alchemy_models.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
 Column, Integer, String, ForeignKey, create_engine)
from sqlalchemy.orm import relationship

# persistence/alchemy_models.py
engine = create_engine('sqlite:///:memory:')
Base = declarative_base()
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    addresses = relationship(
    'Address',
    back_populates='person',
    order_by='Address.email',
    cascade='all, delete-orphan'
    )
    def __repr__(self):
        return f'{self.name}(id={self.id})'
    class Address(Base):
        __tablename__ = 'address'
        id = Column(Integer, primary_key=True)

    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship('Person', back_populates='addresses')
    def __str__(self):
        return self.email
    __repr__ = __str__
    Base.metadata.create_all(engine)