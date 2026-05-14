# Standalone Visualization - No External Tools Required

## Overview

The threat modeling system now generates **standalone PNG visualizations** using Python's matplotlib library. No external tools or binaries are required.

## What Changed

### Before (DOT files)
- Generated `.dot` files (text format)
- Required graphviz binary to convert to images
- Users had to:
  - Install graphviz separately OR
  - Copy DOT code to online viewer OR
  - Install VS Code extensions

### After (PNG files)
- **Direct PNG generation** using matplotlib
- **No external dependencies** beyond Python packages
- **Cross-platform** - works anywhere Python runs
- **High quality** - 300 DPI production-ready images

## Generated Files

```
out/
├── architecture.png  (292 KB)  - Semantic compiler architecture
└── dfd.png          (297 KB)  - PyTM data flow diagram
```

## Features

### Architecture Diagram (`architecture.png`)
- **Trust zones**: Color-coded background regions (Internet → DMZ → Trusted → HighSide)
- **Components**: Shapes indicating type (circles=actors, boxes=processes, cylinders=datastores)
- **Data flows**: Arrows colored by risk level:
  - Gray: Control flow
  - Orange: Ingestion (HIGH risk)
  - Blue: Retrieval
  - Red: Context Injection (CRITICAL)
  - Purple: LLM Inference
- **Legend**: Flow type reference

### DFD Diagram (`dfd.png`)
- **PyTM elements**: All components from threat model
- **Same visual style**: Consistent with architecture diagram
- **Flow semantics**: Labeled with flow types and names

## How to Use

### Generate Diagrams

```powershell
# Semantic architecture
python -m threatmodeling.visualize

# PyTM DFD
python -m threatmodeling
```

### View Diagrams

**Option 1: File Explorer**
- Double-click PNG files in `out/` folder
- Opens in default image viewer

**Option 2: VS Code**
- Click on PNG files in Explorer panel
- Built-in image preview

**Option 3: Streamlit UI**
```powershell
streamlit run app.py
```
- Diagrams displayed inline in browser
- No manual file opening needed

## Technical Details

### Dependencies
```
matplotlib  - Core plotting library
pillow      - Image processing (used by Streamlit)
```

Both installed via:
```powershell
pip install -r requirements.txt
```

### Layout Algorithm
- **Hierarchical positioning**: Components arranged by trust zone
- **Automatic spacing**: Calculated based on number of components
- **Edge routing**: Curved arrows with automatic label placement
- **Zone clustering**: Visual grouping with colored backgrounds

### Rendering
- **Figure size**: 16x10 inches (optimal for screens/documents)
- **DPI**: 300 (print quality)
- **Format**: PNG with white background
- **Anti-aliasing**: Smooth edges and text

## Code References

### Main Visualization Functions

1. **[visualize.py](src/threatmodeling/visualize.py)** - Semantic architecture
   - `generate_architecture_diagram()` - Main entry point
   - Uses NetworkX graph from TypeSpec parser
   - Queries knowledge graph for context

2. **[__main__.py](src/threatmodeling/__main__.py)** - PyTM DFD
   - `visualize_dfd()` - Extracts PyTM elements
   - Mirrors layout from semantic diagram
   - Consistent styling

### Streamlit Integration

**[app.py](app.py)** - Lines 115-125, 145-155
```python
from PIL import Image
img = Image.open("out/architecture.png")
st.image(img, caption="...", use_container_width=True)
```

## Benefits

✅ **Zero setup** - Works immediately after `pip install`  
✅ **Offline ready** - No internet required for visualization  
✅ **Version control friendly** - PNG files easy to track in git  
✅ **Documentation ready** - Embeddable in markdown, Word, PDFs  
✅ **Consistent rendering** - Same output across all platforms  

## Example Output

Both diagrams show:
- 6 components across 4 trust zones
- 8+ data flows with semantic types
- Visual hierarchy (left-to-right: Internet → HighSide)
- Risk-based color coding

**Architecture diagram includes**:
- 7 threat patterns from knowledge graph (referenced in analysis)

**DFD diagram includes**:
- PyTM element metadata (protocols, classifications)

---

**Migration Complete**: All visualization now uses matplotlib - no DOT files or graphviz binary required.
