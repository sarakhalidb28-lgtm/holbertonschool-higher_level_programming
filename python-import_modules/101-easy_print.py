cat << 'EOF' > 101-easy_print.py
#!/usr/bin/python3
import os; os.write(1, b"#pythoniscool\n")
EOF
