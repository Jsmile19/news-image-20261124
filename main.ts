import { copyFileSync, existsSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const source = join(root, 'entry.png');
if (!existsSync(source)) {
  console.error(`Source image not found: ${source}`);
  process.exit(1);
}

const output = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const destination = join(output, 'entry.png');
mkdirSync(output, { recursive: true });
copyFileSync(source, destination);
console.log(destination);
