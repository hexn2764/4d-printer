### Test ID Structure

The Test ID naming convention follows the structure:

`[Source]-[Type]-[Module]-[Category]-[Sequential Number]`

#### Components of the Test ID

1. **Source**:
   - `C`: Client-facing (tests required by the client)
   - `D`: Developer-facing (internal tests, module-level tests, etc.)

2. **Type**:
   - `T`: Test

3. **Module**:
   - `AN`: Analyser module (e.g., `analyser.py`)
   - `CSV`: CSV Handler module (e.g., `csv_handler.py`)
   - etc.

4. **Category**:
   - Describes the specific function or focus of the test (e.g., validation, parsing, etc.).

5. **Sequential Number**:
   - A unique identifier within the scope of the source, type, module, and category.

#### Example
- `D-T-CSV-RDC-001`: A developer-facing test (`D`) for the CSV module (`CSV`), specifically focusing on reading CSV files (`RDC`), and is the first in its sequence (`001`).
- `C-T-AN-GDU-001`: A client-facing test (`C`) for the Analyser module (`AN`), focusing on calculating total duration (`GDU`), and is the first in its sequence (`001`).