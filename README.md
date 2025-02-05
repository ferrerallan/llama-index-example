# LlamaIndex Document Query Application

This application demonstrates how to build a document querying system using LlamaIndex, OpenAI's GPT-4, and ChromaDB for vector storage. The system can read documents from a directory, process them, and answer questions about their content using natural language.

## Features

- Document processing and indexing using LlamaIndex
- Vector storage with ChromaDB for efficient similarity search
- GPT-4 integration for natural language understanding
- Customizable chunking parameters for document processing
- Environment variable management for API keys

## Prerequisites

Before running this application, make sure you have:

- Python 3.8 or higher installed
- An OpenAI API key
- The following Python packages installed:
  ```bash
  pip install llama-index openai chromadb python-dotenv
  ```

## Project Structure

```
llama-index-example/
├── docs/               # Directory containing your documents
├── .env               # Environment variables configuration
├── main.py            # Main application code
└── README.md          # This file
```

## Configuration

1. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_KEY=your_api_key_here
   ```

2. Place your documents in the `docs/` directory. The application will process all documents in this directory.

## How It Works

The application follows these steps:

1. **Environment Setup**: Loads the OpenAI API key from environment variables.

2. **Index Creation** (`create_index` function):
   - Configures LlamaIndex settings with GPT-4 and OpenAI embeddings
   - Sets up ChromaDB for vector storage
   - Processes documents using SimpleNodeParser with specified chunk parameters
   - Creates and returns a VectorStoreIndex

3. **Query Processing** (`main` function):
   - Creates a query engine with configured parameters
   - Executes queries against the document index
   - Returns responses based on document content

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/ferrerallan/llama-index-example.git
   cd llama-index-example
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables as described in the Configuration section.

4. Run the application:
   ```bash
   python main.py
   ```

## Customization

You can modify the following parameters in the code to adjust the behavior:

- `Settings.chunk_size`: Controls the size of document chunks (default: 1024)
- `chunk_overlap`: Controls the overlap between chunks (default: 20)
- `similarity_top_k`: Number of similar chunks to consider (default: 3)
- `response_mode`: Response generation mode (default: "compact")

## Error Handling

The application includes basic error handling that will:
- Catch and display any exceptions that occur during execution
- Print error messages for debugging purposes

## Contributing

Feel free to submit issues and pull requests to improve the application.
