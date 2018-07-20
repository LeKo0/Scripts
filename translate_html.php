<?php

# [START translate_quickstart]
# Includes the autoloader for libraries installed with composer
require __DIR__ . '/vendor/autoload.php';

# Imports the Google Cloud client library
use Google\Cloud\Translate\TranslateClient;

# Your Google Cloud Platform project ID
$projectId = 'signalement-derr-1530221926423';

# Instantiates a client
$translate = new TranslateClient([
    'projectId' => $projectId
]);

# The text to translate
$text = $_POST["text"];

# The target language
$target = 'en';
 
# Translates the text
$translation = $translate->translate($text, [
    'target' => $target
]);

# Replaces all URLs to their translated version
$pattern = '/href="(http|https):\/\/www.arrondissement.com\//';
$translated_url = 'href="https://www.arrondissement.com/eng/';

$output = preg_replace($pattern, $translated_url, $translation['text']);

return $output;
