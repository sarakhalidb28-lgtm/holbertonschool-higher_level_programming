cat << 'EOF' > 5-variable_load.py
#!/usr/bin/python3
if __name__ == "__main__":
    from variable_load_5 import a

    print(a)
EOF
