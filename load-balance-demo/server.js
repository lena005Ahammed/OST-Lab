const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;

app.get("/", (req, res) => {
  setTimeout(() => {
    res.send("Slow Server - Port 3000");
  }, 5000);
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

Save and close. Then restart it:
```
node server.js