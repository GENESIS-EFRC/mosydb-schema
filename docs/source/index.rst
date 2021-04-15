.. Material Schema documentation master file, created by
   sphinx-quickstart on Wed Mar  3 10:43:48 2021.
   Can adapt this file, but it should at least
   contain the root `toctree` directive.

================================================================
Documentation of MOSY DB Schema: A Schema for Material Synthesis
================================================================
A goal put forth by the Materials Genome Initiative (MGI: https://www.mgi.gov/) is to establish large scale data
sharing tools within the materials research community to facilitate more rapid development of novel materials.
With this in mind, we present here a schema for storing synthesis recipes in a structured manner. We hope this
is the first step towards a database to store and share synthesis procedures.

MOSY stands for "motion motivated synthesis". The name was chosen because "to synthesize" broadly means
to make something from simpler components in a series of steps. As scientists, and humans, when we create (or synthesize)
anything we do so with the final product as the goal. Said another way, we are moving towards the motivation (the final
product) by doing one action at a time in the sequential procedure. The hope is that this schema can be used to capture each of
the actions in the synthesis, as well as the final product created.

We invite feedback on the schema, and ideas for modifying and adjusting it to best suit the needs of the
research community.

This repository contains the formal schemas and some Python scripts for validating the documents.

.. toctree::
   :maxdepth: 2

   install
   schema
   release-history
