<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9">
<xsl:output method="html" indent="yes" encoding="UTF-8"/>
<xsl:template match="/">
<html>
<head>
  <title>Sitemap — Casinos Czech</title>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <style>
    body{font-family:system-ui,-apple-system,sans-serif;margin:0;padding:0;background:#f8f9fa;color:#333}
    .header{background:#1a1a2e;color:#fff;padding:30px 20px;text-align:center}
    .header h1{margin:0;font-size:1.5rem;letter-spacing:1px}
    .header p{margin:8px 0 0;color:#aaa;font-size:.9rem}
    .container{max-width:1000px;margin:0 auto;padding:20px}
    .count{background:#fff;padding:12px 20px;border-radius:6px;margin-bottom:20px;font-size:.85rem;color:#666;border:1px solid #e0e0e0}
    .count strong{color:#1a1a2e}
    table{width:100%;border-collapse:collapse;background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.08)}
    th{background:#1a1a2e;color:#fff;padding:12px 16px;text-align:left;font-size:.8rem;text-transform:uppercase;letter-spacing:.5px}
    td{padding:10px 16px;border-bottom:1px solid #f0f0f0;font-size:.85rem}
    tr:hover td{background:#f5f5ff}
    td a{color:#2563eb;text-decoration:none;word-break:break-all}
    td a:hover{text-decoration:underline}
    .priority{text-align:center}
    .high{color:#16a34a;font-weight:700}
    .medium{color:#d97706;font-weight:600}
    .low{color:#888}
    .footer{text-align:center;padding:30px 20px;color:#999;font-size:.75rem}
  </style>
</head>
<body>
  <div class="header">
    <h1>Casinos Czech — Sitemap</h1>
    <p>Mapa stranek pro vyhledavace</p>
  </div>
  <div class="container">
    <div class="count">
      <strong><xsl:value-of select="count(sitemap:urlset/sitemap:url)"/></strong> URL adres v sitemap
    </div>
    <table>
      <thead>
        <tr>
          <th>#</th>
          <th>URL</th>
          <th>Posledni zmena</th>
          <th>Frekvence</th>
          <th>Priorita</th>
        </tr>
      </thead>
      <tbody>
        <xsl:for-each select="sitemap:urlset/sitemap:url">
          <tr>
            <td><xsl:value-of select="position()"/></td>
            <td><a href="{sitemap:loc}"><xsl:value-of select="sitemap:loc"/></a></td>
            <td><xsl:value-of select="sitemap:lastmod"/></td>
            <td><xsl:value-of select="sitemap:changefreq"/></td>
            <td class="priority">
              <xsl:choose>
                <xsl:when test="sitemap:priority >= 0.85"><span class="high"><xsl:value-of select="sitemap:priority"/></span></xsl:when>
                <xsl:when test="sitemap:priority >= 0.75"><span class="medium"><xsl:value-of select="sitemap:priority"/></span></xsl:when>
                <xsl:otherwise><span class="low"><xsl:value-of select="sitemap:priority"/></span></xsl:otherwise>
              </xsl:choose>
            </td>
          </tr>
        </xsl:for-each>
      </tbody>
    </table>
  </div>
  <div class="footer">Casinos Czech .CZ — Sitemap generovana automaticky</div>
</body>
</html>
</xsl:template>
</xsl:stylesheet>