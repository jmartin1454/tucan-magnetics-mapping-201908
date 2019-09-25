# tucan-magnetic-mapping-201908
### This repository contains the data of mapping performed on the August 9, 2019 and the evaluation notebooks

### Description of the contents: 
#### Data directories
* 20190809_mapping_all : the original directoy, for the archiving purpose
#### Monitoring data:
* online_data.csv : monitoring data before the mapping was started 
* online_data09-08-19.csv : monitoring during the mapping measurements 
* timing.csv : UNIX times of teh first measurement and the last measurement of each measurement cycle 

#### Folders where the plots are exported
* plots_u
* plots_v 
* plots_0809_int_u 
* plots_0809_int_v
* plots_0809_int_w
* plots_RUN4_u
* plots_RUN4_v
* plots_floor_2D_color
* plots_floor_gradients
* fall_run 

#### Folders made to export csv fiels which were shared to Russ anda Maedeh
* data_csv

#### Evaluation notebooks:
* monitoring.ipynb : plots monitoring results during mapping 
* mapping_0809_3D.ipynb : exports 3D (2 geometrical + 1 magnetic component) plots 
* mapping_0809_3D_2D_interpolation.ipynb : exports 3D (2 geometrical + 1 magnetic component) plots with interpolated points
* mapping_0809_3D_2D_interpolation_floor.ipynb : exports color plots of the B-field neasr the floor 
* mapping_0809_3D_2D_interpolation_xyz.ipynb : exports 3D plots, studies the field properties near the SCM in detail 
* mapping_0809_3D_2D_interpolation_xyz_conf.ipynb : makes a cross-sectional 3D field map. Made for a presentation at JPS meeting 
* mapping_0809_3D_2D_interpolation_xyz_zoffset.ipynb : exports 3D plots, but z shifted so thaty floor level is z=0 (for presentation purpose)

#### python codes read by some of the notebooks
* matplot_tz_preamble.py
* midas_sub.py






