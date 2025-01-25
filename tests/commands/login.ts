import { expect } from '@playwright/test';

export async function testLogin(page: any) {
    await page.goto('https://www.wp.pl/');
    await page.getByRole('button', { name: 'AKCEPTUJĘ I PRZECHODZĘ DO' }).click();
    await page.locator('a').filter({ hasText: 'Menu' }).click();
    await page.getByRole('link', { name: 'Sport', exact: true }).click();
    await expect(page.getByRole('link', { name: 'SportoweFakty' })).toBeVisible();
}