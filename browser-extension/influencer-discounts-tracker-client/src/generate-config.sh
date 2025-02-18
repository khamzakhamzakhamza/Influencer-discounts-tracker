to_json_string() {
    local value="$1"
    if [ -z "$value" ]; then
        printf 'undefined'
    else
        printf '"%s"' "$value"
    fi
}

API_HOST=$(to_json_string "$IDT_API_HOST")

cat <<EOF
window.IDT_API_HOST=$API_HOST;
EOF