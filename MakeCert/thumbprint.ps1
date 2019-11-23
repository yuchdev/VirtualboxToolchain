# The script fetches cerfificates VirtualBoxSHA1 and VirtualBoxSHA256, previously created by create_certs.cmd scrips
# If parses thumbprint, necessary for LocalConfig, and writes into Certificates.kmk file

write-host "CN=VirtualBoxSHA1"
$getThumb1 = Get-ChildItem -path cert:\LocalMachine\Root | where { $_.Subject -match "CN\=VirtualBoxSHA1" }
$getThumb1.thumbprint

write-host "CN=VirtualBoxSHA256"
$getThumb256 = Get-ChildItem -path cert:\LocalMachine\Root | where { $_.Subject -match "CN\=VirtualBoxSHA256" }
$getThumb256.thumbprint

$text = "VBOX_CERTIFICATE_FINGERPRINT := {0}`r`nVBOX_CERTIFICATE_SHA2_FINGERPRINT := {1}`r`n" -f $getThumb1.thumbprint, $getThumb256.thumbprint
$text | Set-Content "Certificates.kmk"

Write-Host "`r`nThumbprint retreival successful. SHA1 and SHA256 thumbprints are written in Certificates.kmk file. Just add them to your VirtualBox local config or replace old values`r`n"
