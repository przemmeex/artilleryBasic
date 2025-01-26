import { expect } from '@playwright/test';

export async function testDogPage(page: any) {
    await page.goto('https://en.wikipedia.org/wiki/Dog');
    await page.getByRole('link', { name: 'dingoes', exact: true }).click();
    await expect(page.getByRole('heading', { name: 'Dingo', exact: true }).locator('span')).toBeVisible();
}

export async function testCatPage(page: any) {
    await page.goto('https://en.wikipedia.org/wiki/Cat');
    await page.getByRole('link', { name: 'Sand cat' }).first().click();
    await expect(page.getByRole('heading', { name: 'Sand cat', exact: true }).locator('span')).toBeVisible();
}