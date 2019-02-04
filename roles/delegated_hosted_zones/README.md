###Delegated hosted zones

When we have an apex in a master account and a hosted zone in a secondary account, creating
the correct dns entries in other state holding tools is a bit of a hack, what we've created here
is a simple role that will create these top level route53 entries

#####meta-data structure
````yaml
parent_zone_name: #Apex FQDN without protocol
parent_account_id: #Apex aws account id

hosted_zones:
  - account_id: #Aws child account id
    role_name: #delegated role name
    zone_name: #the subdomaina we want to create minus the parent FQDN
    is_delegated: #True for a subdomain on separate account, false for a subdomain on the apex account
    is_apex: #True if we are creating a new apex domain, default false
```` 