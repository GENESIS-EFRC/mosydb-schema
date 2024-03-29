===========================================
MOSY DB Schema: A Materials Sythesis Schema
===========================================

|Documentation|

.. |Documentation| image:: https://github.com/GENESIS-EFRC/mosydb-schema/actions/workflows/docs.yml/badge.svg
   :target: https://github.com/GENESIS-EFRC/mosydb-schema/actions/workflows/docs.yml


|test|

.. |test| image:: https://github.com/GENESIS-EFRC/mosydb-schema/actions/workflows/test.yml/badge.svg
   :target: https://github.com/GENESIS-EFRC/mosydb-schema/actions/workflows/test.yml


A goal put forth by the Materials Genome Initiative (MGI) is to establish large scale data sharing within the materials
research community to facilitate more rapid development of novel materials.
We present here a schema for storing synthesis recipes in a structured manner.

MOSY stands for "motion motivated synthesis". The name was chosen when considering that synthesis broadly means
to make something from simpler components in a series of steps. As scientists, and humans, when we create (or synthesize)
anything we do so with the final product as the goal. Said another way, we are moving towards the motivation (the final
product) by doing one action at a time in the procedure. The hope is that this schema can be used to capture each of
the actions in the synthesis, as well as the final product created.

We invite feedback on the schema, and ideas for modifying and adjusting it to best suit the needs of the
research community.

This repository contains the formal schemas and some Python scripts for validating the documents.
