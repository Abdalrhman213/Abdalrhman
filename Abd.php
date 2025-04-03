<?php
function generateQuadUsernames() {$chars = 'abcdefghijklmnopqrstuvwxyz0123456789';$usernames = [];
    for ($i = 0;$i < 36;$i++) {
        for ($j = 0;$j < 36;$j++) {
            for ($k = 0;$k < 36;$k++) {
                for ($l = 0;$l < 36;$l++) {$usernames[] =$chars[$i] .$chars[$j] .$chars[$k] .$chars[$l];}            }}    }
    return$usernames;}
function checkTikTokUsername($username) {$url ="https://www.tiktok.com/@{$username}";$ch = curl_init();
    curl_setopt($ch, CURLOPT_URL,$url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
    curl_setopt($ch, CURLOPT_USERAGENT,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36");$response = curl_exec($ch);$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($httpCode == 200) {
        return"Username {$username} is fucking live and kicking!";} else {
        return"Username {$username} is a dead-ass piece of shit.";}}

set_time_limit(0); // No fucking timeout, we’re going hard$usernames = generateQuadUsernames();
foreach ($usernames as$username) {
    echo checkTikTokUsername($username) ."\n";
    sleep(1); // Slow the fuck down to avoid TikTok’s bitch-ass rate limits}?>
