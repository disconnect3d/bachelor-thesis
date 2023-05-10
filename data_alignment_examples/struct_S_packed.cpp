// ustawienie wyrównania do jednego bajtu
#pragma pack(1)
struct S {
    int a;
    bool b;
    int* c;
    bool e;
    int f;
    bool g;
    int h;
    bool i;
};
// przywrócenie domyślnego ustawienia wyrównania
#pragma pack()

int main() {
    S s;
    return sizeof(S);
}
