# 🌐 tiny-py-server

A tiny, educational HTTP server built from scratch in Python — no frameworks, no magic. Great for learning how HTTP, routing, and socket programming work under the hood.

---

## 🚀 Features

- 🔌 Raw socket-based HTTP server  
- 🧠 Simple custom router with `@route()` decorator  
- 🎯 Clean separation of concerns (router, constants, utils)  
- 📄 Custom `HttpResponse` builder  
- 🛠 Easily extensible for methods, headers, static files  

---

## 🧑‍💻 How to Run

### 🔧 1. Clone the repo

```
git clone https://github.com/yourusername/tiny-py-server.git
cd tiny-py-server
```

### 🐍 2. Run the server

```
python3 example.py
```

Server starts on:

```
Serving HTTP on 127.0.0.1:8080...
```

---

## 📡 Example Routes

```
@router.route("/test1")
def test1():
    return HttpResponse().prepareResponse(200, "text/html", "<h1>Test 1</h1>")

@router.route("/")
def root():
    return HttpResponse().prepareResponse(404, "text/html", "<h1>Not implemented</h1>")
```

Access it via browser or curl:

```
curl http://localhost:8080/test1
```

---

## ✅ To-Do (Ideas)

- [/] Support `POST` method  
- [ ] Add static file serving (`/static/`)  
- [ ] Logging with timestamps  
- [ ] JSON response helper  
- [ ] Add simple templating  

---

## 📚 Learning Goals

- Understand how HTTP requests are parsed  
- Explore TCP sockets in Python  
- Build a toy routing system  
- See how frameworks like Flask work internally  

---

## 🧠 Credits

Built by **Shivam Singhal**  
Inspired by Flask, raw sockets, and curiosity.

---

## 📝 License

MIT License
