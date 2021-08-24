"""Biothings parser function for Meta-KB CDM"""

from mainParser import Parser


def load_statements(data_folder):
    """Load cdm"""
    data = Parser.load_file(Parser, "pmkb_cdm.json", data_folder)
    Parser.load_statements(Parser, data, data_folder)


def load_propositions(data_folder):
    """Load cdm"""
    data = Parser.load_file(Parser, "pmkb_cdm.json", data_folder)
    Parser.load_propositions(Parser, data, data_folder)


def load_variation_descriptors(data_folder):
    """Load cdm"""
    data = Parser.load_file(Parser, "pmkb_cdm.json", data_folder)
    Parser.load_variation_descriptors(Parser, data, data_folder)


def load_gene_descriptors(data_folder):
    """Load cdm"""
    data = Parser.load_file(Parser, "pmkb_cdm.json", data_folder)
    Parser.load_gene_descriptors(Parser, data, data_folder)


def load_therapy_descriptors(data_folder):
    """Load cdm"""
    data = Parser.load_file(Parser, "pmkb_cdm.json", data_folder)
    Parser.load_therapy_descriptors(Parser, data, data_folder)

def load_disease_descriptors(data_folder):
    """Load cdm"""
    data = Parser.load_file(Parser, "pmkb_cdm.json", data_folder)
    Parser.load_disease_descriptors(Parser, data, data_folder)


def load_methods(data_folder):
    """Load cdm"""
    data = Parser.load_file(Parser, "pmkb_cdm.json", data_folder)
    Parser.load_methods(Parser, data, data_folder)


def load_documents(data_folder):
    """Load cdm"""
    data = Parser.load_file(Parser, "pmkb_cdm.json", data_folder)
    Parser.load_documents(Parser, data, data_folder)
