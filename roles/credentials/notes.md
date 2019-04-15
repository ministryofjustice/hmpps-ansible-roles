
# Order

```
main.yml >
  process_products.yml >
    process_namespaces.yml >
      process_roles.yml >
        create_string_entry.yml >
          ssm_entry.yml >
            extract_ssm_entry.yml || create_ssm_entry.yml
        create_password.yml>
          ssm_entry.yml >
            extract_ssm_entry.yml || create_ssm_entry.yml
        create_ssh_key_entry.yml>
          ssm_entry.yml >
            extract_ssm_entry.yml || create_ssm_entry.yml
```
