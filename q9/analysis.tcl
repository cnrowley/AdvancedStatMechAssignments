
proc percentsheet {structure} {
    set total 0
    set scount 0
    foreach s $structure {
        if { ($s == "E" || $s == "B") } {incr scount}
        incr total
    }
    return [ expr {100.0 * $scount / $total} ]
}


proc percenth {structure} {
    set total 0
    set hcount 0
    foreach s $structure {
	if { ($s == "H" || $s == "G" || $s == "I") } { incr hcount }
	incr total
    }
    return [ expr { 100.0 * $hcount / $total} ]
}


mol new pout type parm7 waitfor all
mol  addfile {traj1.dcd} waitfor all 

set fd [open "folding.dat" "w"]
puts $fd "time,r_gyr,n_hb,sasa,sheet"
set selprot [atomselect	top "protein"]
set nf [molinfo top get numframes] 

for {set i 0} {$i < $nf} {incr i} { 
animate goto $i
mol reanalyze top

set rg [measure rgyr $selprot]
set hb [measure hbonds 3.0 30.0 $selprot]
set nhb [llength [lindex $hb 0]]
set sa [measure sasa 1.4 $selprot]

set ss [$selprot get structure]
set ps [percentsheet $ss]
set time [ expr {$i * 4.0 * 25000 / 1000000 } ]
puts $fd "$time,$rg,$nhb,$sa,$ps"
}

close $fd

quit

