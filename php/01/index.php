<?php
$filename = "input";
$inputs = [];
$left = [];
$right = [];
if ($file = fopen($filename, "r")) {
    while (!feof($file)) {
        $line = fgets($file);
        if (!empty($line)) {
            $inputs = explode("   ", trim($line));
            $left[] = (int) $inputs[0];
            $right[] = (int) $inputs[1];
        }
    }
    fclose($file);
}

sort($left);
sort($right);
$inputs = array_combine($left, $right);
$total_dist = 0;
foreach ($inputs as $ori => $dest)
{
//    var_dump($ori, $dest);
    $total_dist += abs($ori - $dest);
}

var_dump($total_dist);
