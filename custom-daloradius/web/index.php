<?php
$mysqli = new mysqli(getenv('DB_HOST'), getenv('DB_USER'), getenv('DB_PASS'), getenv('DB_NAME'));
$result = $mysqli->query("SELECT nasname, status, last_check FROM nas_status ORDER BY nasname ASC");
?>
<!DOCTYPE html>
<html>
<head>
<title>NAS Monitor</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="p-4 bg-light">
<div class="container">
  <h2 class="mb-4 text-center text-primary">NAS SNMP Status Monitor</h2>
  <table class="table table-bordered table-striped">
    <thead class="table-dark">
      <tr><th>NAS Name</th><th>Status</th><th>Last Check</th></tr>
    </thead>
    <tbody>
      <?php while($row = $result->fetch_assoc()): ?>
        <tr>
          <td><?= htmlspecialchars($row['nasname']) ?></td>
          <td><span class="badge bg-<?= $row['status']=='up'?'success':'danger' ?>"><?= $row['status'] ?></span></td>
          <td><?= $row['last_check'] ?></td>
        </tr>
      <?php endwhile; ?>
    </tbody>
  </table>
</div>
</body>
</html>
