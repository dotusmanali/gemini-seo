# Technical SEO Checklist

## 1. Indexability & Crawling
- [ ] **robots.txt**: Ensure `Disallow` doesn't block critical resources. Declare `Sitemap` location.
- [ ] **Sitemap.xml**: Validate 200 OK status, clean URLs, and lastmod timestamps.
- [ ] **Canonicalization**: Every page should have a self-referencing canonical or point to a preferred version.
- [ ] **Noindex**: Check for accidental `<meta name="robots" content="noindex">`.
- [ ] **Status Codes**: Minimize 301/302 chains, fix 404s, avoid 5xx errors.

## 2. URL & Site Architecture
- [ ] **HTTPS**: Valid SSL certificate, no mixed content.
- [ ] **URL Slugs**: Descriptive, kebab-case, no session IDs.
- [ ] **Internal Linking**: No orphan pages, descriptive anchor text.
- [ ] **Pagination**: Use `rel="prev/next"` logic (deprecated by Google but still useful for others) or `Load More`.

## 3. Metadata & Headers
- [ ] **Title Tags**: 50-60 chars, includes primary keyword and brand.
- [ ] **Meta Descriptions**: 150-160 chars, compelling CTA.
- [ ] **H1-H4 Structure**: One H1 per page, logical nesting (H2 under H1, etc.).
- [ ] **Alt Text**: Descriptive alt tags for all meaningful images.

## 4. Performance & Mobile
- [ ] **Mobile Responsive**: Viewport meta tag present, legible font sizes.
- [ ] **Core Web Vitals**: Pass LCP, INP, and CLS thresholds.
- [ ] **Compression**: Gzip/Brotli enabled for text assets.
- [ ] **Caching**: Proper Cache-Control headers.
