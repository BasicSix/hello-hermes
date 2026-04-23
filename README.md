# hello-hermes

A simple Python project to demonstrate Hermes agent capabilities

## 🚀 Features

### Core Utilities
- **calculate_average**: Calculate average of numeric lists
- **fibonacci**: Generate Fibonacci sequences
- **factorial**: Calculate factorial values

## 📦 Installation

```bash
pip install -e .
```

## 🧪 Testing

Run all tests:
```bash
python run-tests.py
```

## 💻 Usage

### Python API
```python
from hello_hermes.utils import calculate_average, fibonacci, factorial

# Calculate average
result = calculate_average([1, 2, 3, 4, 5])
print(f"Average: {result}")  # Average: 3.0

# Generate Fibonacci sequence
sequence = fibonacci(8)
print(f"Fibonacci: {sequence}")  # [0, 1, 1, 2, 3, 5, 8, 13]

# Calculate factorial
fact = factorial(5)
print(f"Factorial: {fact}")  # Factorial: 120
```

## 🔧 Development

### Setup
```bash
git clone <repository-url>
cd hello-hermes
pip install pytest black flake8 mypy
```

### Code Quality
```bash
# Format code
black src/

# Lint code
flake8 src/

# Run tests with pytest
pytest tests/ -v

# Type checking
mypy src/
```

## 📊 Test Coverage

| Function | Tests | Status |
|----------|-------|--------|
| `calculate_average` | 5 | ✅ All Pass |
| `fibonacci` | 5 | ✅ All Pass |
| `factorial` | 6 | ✅ All Pass |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request