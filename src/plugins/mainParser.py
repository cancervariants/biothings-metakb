""""""
import os
import json


class Parser:
    """A Parser class to parse MetaKB source-specific transformed data"""

    def load_statements(self, data, data_folder):
        """Load cdm"""
        for s in data["statements"]:
            _id = s["id"]
            record = {}
            record["statement"] = s
            doc = {"_id": _id}
            doc.update(record)

            yield doc


    def load_propositions(self, data, data_folder):
        """Load cdm"""
        for s in data["statements"]:
            _id = s["id"]
            prop = s["proposition"]
            record = {}
            for p in data["propositions"]:
                if prop == p["id"]:
                    record["proposition"] = p
                    break
            doc = {"_id": _id}
            doc.update(record)

            yield doc


    def load_variation_descriptors(self, data, data_folder):
        """Load cdm"""
        for s in data["statements"]:
            _id = s["id"]
            v_des = s["variation_descriptor"]
            record = {}
            for v in data["variation_descriptors"]:
                if v_des == v["id"]:
                    record["variation_descriptor"] = v
                    break
            doc = {"_id": _id}
            doc.update(record)

            yield doc


    def load_gene_descriptors(self, data, data_folder):
        """Load cdm"""
        for s in data["statements"]:   
            _id = s["id"]
            v_des = s["variation_descriptor"]
            record = {}
            for v in data["variation_descriptors"]:
                if v_des == v["id"]:
                    g_des = v["gene_context"]
                    break
            for g in data["gene_descriptors"]:
                if g_des == g["id"]:
                    record["gene_descriptor"] = g
                    break
            doc = {"_id": _id}
            doc.update(record)

            yield doc


    def load_therapy_descriptors(self, data, data_folder):
        """Load cdm"""
        for s in data["statements"]:
            _id = s["id"]
            t_des = s["therapy_descriptor"]
            record = {}
            for t in data["therapy_descriptors"]:
                if t_des == t["id"]:
                    record["therapy_descriptor"] = t
                    break
            doc = {"_id": _id}
            doc.update(record)

            yield doc


    def load_disease_descriptors(self, data, data_folder):
        """Load cdm"""
        for s in data["statements"]:
            _id = s["id"]
            d_des = s["disease_descriptor"]
            record = {}
            for d in data["disease_descriptors"]:
                if d_des == d["id"]:
                    record["disease_descriptor"] = d
                    break
            doc = {"_id": _id}
            doc.update(record)

            yield doc


    def load_methods(self, data, data_folder):
        """Load cdm"""
        for s in data["statements"]:
            _id = s["id"]
            method = s["method"]
            record = {}
            for m in data["methods"]:
                if method == m["id"]:
                    record["method"] = m
                    break
            doc = {"_id": _id}
            doc.update(record)

            yield doc


    def load_documents(self, data, data_folder):
        """Load cdm"""
        for s in data["statements"]:
            _id = s["id"]
            docs = s["supported_by"][0]
            record = {}
            for document in data["documents"]:
                if docs == document["id"]:
                    record["document"] = document
                    break
            doc = {"_id": _id}
            doc.update(record)

            yield doc


    def load_file(self, file_name, data_folder):
        """Load MetaKB CDM file"""
        infile = os.path.join(data_folder, file_name)
        assert os.path.exists(infile)
        with open(infile, "r") as f:
            data = json.load(f)

        return data
