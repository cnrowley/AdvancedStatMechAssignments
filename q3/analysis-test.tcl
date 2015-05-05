proc percentsheet {structure} {
    set total 0
    set scount 0
    foreach s $structure {
        if { ($s == "E" || $s == "B") } {incr scount; puts $scount }
        incr total
    }
    puts $scount
    return [ expr {1.0*$scount / $total} ]
}


proc percenth {structure} {
    set total 0
    set hcount 0
    foreach s $structure {
	puts $s
	if { ($s == "H" || $s == "G" || $s == "I") } { 
	    puts $hcount
	    incr hcount 
	}
	incr total
    }
    puts $hcount
    return [ expr { 1.0* $hcount / $total} ]
}

mol new hairpin_sim.psf
mol addfile prod_folding.dcd waitfor 1000

set fd [open "folding.dat" "w"]

set selprot [atomselect	top "protein"]
set nf [molinfo top get numframes] 

for {set i 0} {$i < 1000} {incr i} { 
animate goto $i
mol reanalyze top

set rg [measure rgyr $selprot]
set hb [measure hbonds 3.0 30.0 $selprot]
set nhb [llength [lindex $hb 0]]
set sa [measure sasa 1.4 $selprot]

set ss [$selprot get structure]
set ph [percenth $ss]
set ps [percents $ss]
set time [ expr {$i * 5.0 * 5000 / 1000 } ]
puts $ss
puts $fd "$time $rg $nhb $sa $ph $ps"
}

close $fd

quit

