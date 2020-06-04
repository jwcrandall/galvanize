# Panama-Papers-Network-Analysis

## The Project
Social network analysis of the Panama Papers, with a specific emphasis in Saudi Arabia and, maybe, Jordan.

## Scope


## The Data
The Panama  Papers are a set of 11.5 million document leaks from Panamanian law company ”Mossack Fonseca”, which provides
information on approximately 360,000 businesses and individuals in more than 200 countries linked to offshore structures and covering a time period of nearly 40 years, from 1977 to 2016.

The  ”ICIJ  Offshore”  database,  presents  the  network  of  relationships  between  companies  and  individual  people  with  offshore  companies based in tax havens. Consists in a directed and unweighted network based on commercial  registration  of  all  types  of  companies  involved  in  the  scandal  and the existing relations type, which are:

* "director of” - referring to the person appointed to the company’s management;

* ”address” - through which was possible to establish the country origin of the company;

* ”shareholder of” - if it holds a stake in an offshore company;

* ”intermediary of” - if it mediates companies in access to offshores;

* ”similar of” - if the company is related to another company, among other attributes.

How The Data Is Structured:

* Entity (offshore): company, trust or fund created in a low-tax, offshore
   jurisdiction by an agent.

* Officer: person or company who plays a role in an offshore entity.

* Intermediary: a go-between for someone seeking an offshore corporation
  and an offshore service provider - usually a law-firm or a middleman that
  asks an offshore service provider to create an offshore firm for a client.

* Address: contact postal address as it appears in the original databases
  obtained by ICIJ

| Name          | Type          | Purpose | # of rows | Columns of interest |
| ------------- |:-------------:| -------:|----------:|------------:|
|  panama_papers_edges.csv    |    Edge       |   Each edge has a type of the represented relationship | 1,269,796    |   START_ID, TYPE, END_ID      |
| panama_papers_addresses.csv |    Nodes      |   Legal addresses of officers and entities  |   151,127  |      n/a   |
| panama_papers_entity.csv  |    Nodes      |   Legal entities (corporations, firms, and so on) |   319,421   |     name, jurisdiction    |
| panama_papers_intermediary.csv|    Nodes      |  Persons and organizations that act as links between other organizations| 23,642 |  name, country_code  |
| panama_papers_officer.csv  |    Nodes      | Persons (directors, shareholders, and so on)| 345,645 | name, country_code |

  ![Nodes and Relationships](https://github.com/REDeLapp/Panama-Papers-Network-Analysis/blob/master/pictures/filename.png)

## Network Analysis Methods

* Clustering Coefficient: the fraction of possible triangles in an egocentric network that contain the ego node and exit. It measures the         undefined for directed graphs

* Bridges: high  betweenness  individuals  are  often  critical  to  collaboration
  across different groups.
* Modularity: measure aims to identify the nodes that are more densely connected together than to the rest of the network, describing the network structure,i.e., how the network is compartmentalized into sub-networks
* Closeness and harmonic closeness centrality
* Eigenvector centrality
* PageRank

## EDA

## Model

## References
1. https://offshoreleaks.icij.org/pages/database
2. http://wps.fep.up.pt/wps/wp592.pdf
2. Complex Network Analysis in Python, Dmitry Zinoview, The Pragmatic Programmers. (2018)
