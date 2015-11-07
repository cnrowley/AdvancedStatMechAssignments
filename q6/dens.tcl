source density_profile.tcl
package require density_profile

proc pptable {fp l1 l2} { foreach i1 $l1 i2 $l2 { puts $fp " [format %6.2f $i1]\t[format %6.10f $i2]" }  }

mol new step5_assembly.xplor_ext.psf waitfor all
mol addfile system-npt-03.dcd waitfor all

set nframes [molinfo top get numframes]
puts $nframes

set headdens  [density_profile -selection "type Q0 or type QA" -resolution 2 -frame_from 0 -frame_to 9999 -frame_step 1 -average 1]
set gldens  [density_profile -selection "name GL1 or name GL2" -resolution 2 -frame_from 0 -frame_to 9999 -average 1]
set iondens [density_profile -selection "segid NA or segid CL" -resolution 2  -frame_from 0 -frame_to 9999  -average 1]
set waterdens [density_profile -selection "name W" -resolution 2 -frame_from 0 -frame_to 9999 -average 1]
set taildens [density_profile -selection "type C1 or type C3" -resolution 2  -frame_from 0 -frame_to 9999 -average 1]

set fp [open "headgroup.txt" w]
pptable $fp [lindex $headdens 1] [lindex $headdens 0]
close $fp

set fp [open "glycerol.txt" w]
pptable $fp [lindex $gldens 1] [lindex $gldens 0]
close $fp

set fp [open "ion.txt" w]
pptable $fp [lindex $iondens 1] [lindex $iondens 0]
close $fp

set fp [open "water.txt" w]
pptable $fp [lindex $waterdens 1] [lindex $waterdens 0]
close $fp

set fp [open "tail.txt" w]
pptable $fp [lindex $taildens 1] [lindex $taildens 0]
close $fp
