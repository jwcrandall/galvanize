import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# https://www.occrp.org/en/panamapapers/database

def load_clean_data():
    '''
    This function...
    '''
    # Read the edge list and convert it to network
    edges = pd.read_csv('data/csv_panama_papers_2018-02-14/panama_papers_edges.csv')
    edges = edges[edges["TYPE"] != "registrated address"]
    G = nx.from_pandas_dataframe(edges, "START_ID", "END_ID")

    # Read node lists
    officers       = pd.read_csv("../data/csv_panama_papers_2018-02-14/panama_papers_nodes_officer.csv", index_col = "node_id")
    intermediaries = pd.read_csv("../data/csv_panama_papers_2018-02-14/panama_papers_nodes_intermediary.csv", index_col = "node_id")
    entities       = pd.read_csv("../data/csv_panama_papers_2018-02-14/panama_papers_nodes_entity.csv", index_col = "node_id")

    # Combine the node lists into one dataframe
    officers["type"] = "officer"
    intermediaries["type"] = "intermediary"
    entities["type"] = "entity"

    all_nodes = pd.concat([officers, intermediaries, entities])


    # Do some cleanup of names
    all_nodes["names"] = all_nodes["name"].str.upper().str.strip()

    # Ensure that all "Bearers" do not become a single node
    all_nodes["names"].replace(
        to_replace = [r"MRS?\.\s+", r"\.", r"\s+", "LIMITED", "THE BEARER", "BEARER", "BEARER 1", "EL PORTADOR", "AL PORTADOR"],
        value = ["","", "", "LTD", np.nan, np.nan, np.nan, np.nan, np.nan],
        inplace = True, regex = True)

    # We only want to look at Saudi Arabia and, maybe, Jordan
    CCODES = "SA" # country code to be examined in subgraph
    seeds = all_nodes[all_nodes["country_codes"].isin(CCODES)].index

    # Next Computes the shortest path from the node seed to all reachable nodes that
    # are cutoff hops away and closer.  The function returns a dictionary with the target nodes as keys,
    # so the keys are the cutoff-neighborhood of the seed.
    nodes_of_interest = set.union(*[\
                                   set(nx.single_source_shortest_path_length(F, seed, cutoff = 2).keys())
                                   for seed in seeds])

    # Extract the subgraph that contains all the keys for all the dictionaries
    # with all the connecting eges ... and relabel it
    sub_G = nx.subgraph(G, nodes_of_interest)
    nodes = all_nodes.reindex(sub_G)
    # nodes = all_nodes.loc[ego] # <-- Error is coming from here!
    nodes = nodes[~nodes.index.duplicated()] # There are duplicate countrie codes on some nodes

    # nx.set_node_attributes(sub_G, "cc", nodes["country_codes"])
    nx.set_node_attributes(sub_G, nodes["country_codes"], "betweenness")
    valid_names = nodes[nodes["name"].notnull()]["name"].to_dict() # get rid of null and turn the list into a dictionary
    nx.relabel_nodes(sub_G, valid_names, copy = False)

    with open ("panam-sa.grapml", "wb") as ofile:
        nx.write_graphml(sub_G, ofile)

def country_filter(data):
    pass

def GernalGraph(data):
    # with open ("panam-ca.grapml", "wb") as ofile:
    #     nx.write_graphml(sub_G, ofile)
    pass


if __name__ == '__main__':
    load_clean_data()
