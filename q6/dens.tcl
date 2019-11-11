source density_profile.tcl
package require density_profile

proc pptable {fp l1 l2} { foreach i1 $l1 i2 $l2 { puts $fp " [format %6.2f $i1],[format %6.10f $i2]" }  }

mol new step5_assembly.xplor_ext.psf
mol addfile system-npt-03.dcd waitfor all

set nframes [molinfo top get numframes]
incr nframes -1 
puts $nframes

set headdens  [density_profile -resolution 2 -frame_from 0 -frame_to $nframes -frame_step 1 -average 1 -selection {type Q0 or type QA} ]
set gldens  [density_profile -resolution 2 -frame_from 0 -frame_to $nframes -average 1 -selection {name GL1 or name GL2} ]
set iondens [density_profile -resolution 2  -frame_from 0 -frame_to $nframes -average 1 -selection {segid NA or segid CL} ]
set waterdens [density_profile  -resolution 2 -frame_from 0 -frame_to $nframes -average 1 -selection {resname W} ]
set taildens [density_profile  -resolution 2  -frame_from 0 -frame_to $nframes -average 1 -selection {type C1 or type C3} ]

puts "printing"

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

quit

