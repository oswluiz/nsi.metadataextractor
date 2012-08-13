#coding: utf-8
import sys
from os import environ, path
path = (environ['HOME'] + '/nsi.metadataextractor/app')
if not path in sys.path:
    sys.path.insert(1, path)

#########################################
from xml_parser import Parser
import unittest
from should_dsl import should, should_not
import xml.etree.cElementTree as ET
#########################################


class TestParser(unittest.TestCase):

    def setUp(self):
        self.tccParse = Parser('tcc.xml')
        self.eventannalsParse = Parser('anais_evento.xml')

    def test_parser_has_a_xml_directory(self):
        self.tccParse.file_path |should| be_like(r'.*.xml')

    def test_onepage_metadata_has_a_valid_hash(self):
        type(self.tccParse.onepage_metadata) |should| equal_to(dict)

    def test_onepage_metadata_hash_has_valid_keys_and_values(self):
        metadata_hash = self.tccParse.onepage_metadata
        
        metadata_hash.get("author_position") |should| equal_to (0)
        metadata_hash.get("author_antecessor") |should| equal_to (['\n'])
        metadata_hash.get("author_sucessor") |should| equal_to (['\n'])
        metadata_hash.get("campus_prefix") |should| equal_to (['CAMPUS', 'CAMPI'])
        metadata_hash.get("grade_doctoral") |should| equal_to (['DOUTORADO','DOUTOR'])
        metadata_hash.get("grade_graduation") |should| equal_to (['GRADUAÇÃO', 'CURSO SUPERIOR', 'BACHARELADO', 'LICENCIATURA', 'TECNÓLOGO'])
        metadata_hash.get("grade_master_degree") |should| equal_to (['MESTRADO', 'MESTRE'])
        metadata_hash.get("grade_postdoctoral") |should| equal_to (['PÓS-DOUTORADO', 'PÓS DOUTORADO'])
        metadata_hash.get("grade_spec") |should| equal_to (['PÓS-GRADUAÇÃO', 'LATO SENSU', 'ESPECIALIZAÇÃO', 'ESPECIALISTA', 'MBA'])
        metadata_hash.get("institution_prefix") |should| equal_to (['UNIVERSIDADE', 'INSTITUTO'])
        metadata_hash.get("page") |should| equal_to (2)
        metadata_hash.get("title_prefix") |should| equal_to (['\n'])

    def test_variouspages_metadata_has_a_valid_hash(self):
        type(self.tccParse.onepage_metadata) |should| equal_to(dict)

    def test_variouspages_metadata_hash_has_valid_keys_and_values(self):
        metadata_hash = self.tccParse.variouspages_metadata

        metadata_hash.get("abstract_position") |should| equal_to (1)
        metadata_hash.get("abstract_prefix") |should| equal_to (['RESUMO\n'])
        metadata_hash.get("pages") |should| equal_to ([1,10])


if __name__ == '__main__':
    unittest.main()