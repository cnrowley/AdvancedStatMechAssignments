mol new methanol-interface.psf
mol addfile methanol-interface-35-0.dcd waitfor all
set nframes [molinfo top get numframes] 
set sel [atomselect top all]
put $nframes
for {set i 0} {$i < $nframes} {incr i }  { 
animate goto $i 
display update
$sel writepdb window_$i.pdb 
} 

quit
