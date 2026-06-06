cat << 'EOF' > 101-easy_print.py
import os
os.write(1, b"#pythoniscool\n")
EOF
