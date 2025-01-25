import { testLogin } from '../commands/login';

export async function artilleryScript(page: any) {
    await testLogin(page);
}