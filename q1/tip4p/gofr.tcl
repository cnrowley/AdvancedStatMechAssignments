set psf tip4p.psf
set dcd tip4p.out.dcd

mol load psf $psf dcd $dcd
set outfile1 [open gofr.dat w]

set sel1 [atomselect top "name OH2"]
set sel2 [atomselect top "name OH2"]
set gr0 [measure gofr $sel1 $sel2 delta 0.05 rmax 12.0 usepbc 1 selupdate 1 first 0 last -1 step 1]
set r [lindex $gr0 0]
set gr [lindex $gr0 1]
set igr [lindex $gr0 2]
set isto [lindex $gr0 3]
foreach j $r k $gr l $igr m $isto {
  puts $outfile1 [format "%.4f\t%.4f\t%.4f\t%.4f" $j $k $l $m]
}
close $outfile1
exit 

