<?php
$filename = "input";
$inputs = [];
$left = [];
$right = [];
if ($file = fopen($filename, 'rb')) {
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
$total_dist_occurence = 0;
foreach ($inputs as $ori => $dest)
{
    $total_dist_occurence += $ori*count(array_filter($right, function ($dest) use ($ori) {
        return $dest === $ori;
    }));
}

echo $total_dist_occurence;
