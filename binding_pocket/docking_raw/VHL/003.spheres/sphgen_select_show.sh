sphgen -i INSPH -o OUTSPH
sphere_selector receptor.sph ../001.lig-prep/MZ1_reference.mol2 4.0
showsphere < showsphere.in
cat *clustertemp* >> temp.file
mv temp.file palbo.sel.clust.pdb
rm *clustertemp*
