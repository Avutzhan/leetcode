<?php

function countdown($i) {
  echo $i ."\n";
  if ($i <= 0) {
    return;
  } else {
    countdown($i-1);
  }

}

countdown(10);