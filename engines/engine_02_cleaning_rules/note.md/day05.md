## **Hari 5 – Desain Rule untuk Format Date & Numeric**

**Tujuan:**  
Menangani format data agar konsisten, khususnya **tanggal dan numeric**, sehingga engine bisa memvalidasi dan menormalisasi dataset.

**Tindakan:**
- Buat file `rules/format_validation.yaml`:
  ```yaml
  date_format:
    columns:
      - name: "date_column"
        format: "%Y-%m-%d"
        coerce_errors: true

  numeric_validation:
    columns:
      - name: "age"
        min: 0
        max: 120
        allow_null: false
      - name: "salary"
        min: 0
        max: null
        allow_null: true
