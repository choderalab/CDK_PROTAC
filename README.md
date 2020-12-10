# CDK_PROTAC

This is a project exploring how various protein binding partners of human kinases (e.g. p27 for CDK4, p18 for CDK6) affect the binding of ATP, small-molecule kinase inhibitors (e.g. palbociclib), as well as proteolysis-targeting chimeras (PROTACs).

## Manifest

* `binding_pocket/` - analysis (i.e. structure superposition and docking) to quantify how CDK6 binding pocket changes shape and volume upon p18 binding.
* `PROTAC_models` - construction and equilibration of structural models of kinase : PROTAC : E3 ligase adaptor ternary structures (with and without binding of p18/p27) in the following combination:
    * p18 : CDK6 : BSJ-03-123 : CRBN
    * p27 : CDK4 : BSJ-03-123 : CRBN
    * p18 : CDK6 : BSJ-05-017 : VHL
    * p27 : CDK4 : BSJ-05-017 : VHL
    * CDK6 : BSJ-03-123 : CRBN
    * CDK4 : BSJ-03-123 : CRBN
    * CDK6 : BSJ-05-017 : VHL
    * CDK4 : BSJ-05-017 : VHL
